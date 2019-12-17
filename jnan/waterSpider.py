import re, optparse
import requests
from datetime import datetime, timedelta

from PIL.ImageGrab import grab
from lxml import etree

import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from waterdb import WaterDB

plt.rcParams['font.sans-serif'] = ['FangSong'] #设置默认字体
plt.rcParams['axes.unicode_minus'] = False  #解决保存图象是'_'显示为方块的问题

def spider(id):
    """抓取单页水位数据，返回html文本"""

    html= requests.post(
        url='http://jnwater.jinan.gov.cn/module/web/jpage/dataproxy.jsp?startrecord=%d&endrecord=%d&perpage=15' % (id, id + 45),
        headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)'},
        data={
            'col': '1',
            'appid': '1',
            'webid': '23',
            'path': '/',
            'columnid': '22802',
            'sourceContentType': '1',
            'unitid': '56254',
            'permissiontype': '0'
        }
    )

    return html.text

def parse_html(html):
    """解析html文本，返回解析结果"""

    parse_html = etree.HTML(html)
    items = parse_html.xpath('/html/body/datastore/recordset/record')

    data = list()
    p_date = re.compile(r'(\d{4})\D+(\d{1,2})\D+(\d{1,2})')  # 匹配年月日数字部分的正则表达式
    for item in items:
        date, bt, hh = item.xpath('string(.)').strip().split('  ')[::2]
        year, month, day = p_date.findall(date)[0]
        date = '%s-%02d-%02d'%(year, int(month), int(day))
        bt, hh = bt[:-1].replace(',','.'), hh[:-1].replace(',','.')
        try:
            bt, hh = float(bt[:5]), float(hh[:5])
            data.append((date, bt, hh))
        except:
            pass

    return data

def grad(water_db, deadline):
    """抓取数据，每次一页（45条），直到页内包含截止日期"""
    id = 1
    flag = True
    while flag:
        html = spider(id)
        data = parse_html(html)
        water_db.append(data)
        if deadline in [item[0] for item in data]:
            flag = False
        id += 45
        print('.', end='', flush=True)

    print()

def spring_verify(water_db):
    """数据检查"""

    #去除重复数据
    water_db.dedup()

    #更新已知的日期错误
    err_list = [
        ('2010-10-10', 28.22, 28.17, '2017-10-10'),
        ('2012-01-31', 28.57, 28.51, '2013-01-31'),
        ('2012-12-03', 28.88, 28.86, '2016-12-03'),
        ('2012-12-30', 28.68, 28.66, '2016-12-30'),
        ('2014-09-09', 28.24, 28.18, '2015-09-09'),
        ('2015-02-25', 27.99, 27.92, '2018-02-25'),
        ('2016-02-17', 28.50, 28.46, '2017-02-17'),
        ('2016-06-03', 28.09, 28.02, '2014-06-03'),
        ('2017-02-14', 27.98, 27.91, '2018-02-14'),
        ('2017-07-19', 28.25, 28.20, None)
    ]
    water_db.rectify(err_list)

    #补缺
    missing_list = [
        ('2014-03-11', 28.52, 28.42),
        ('2016-11-05', 28.95, 28.96),
        ('2016-11-22', 28.90, 28.89),
        ('2017-03-29', 28.09, 28.03)
    ]
    water_db.fill(missing_list)

    #数据检查
    lost_list = list()
    repeat_dict = dict()

    total, date_first, date_last =water_db.stat()   # 数据总数、最早数据日期、最新数据日期
    if date_first and date_last:
        date_start = datetime.strptime(date_first, '%Y-%m-%d')
        date_stop = datetime.strptime(date_last, '%Y-%m-%d')

        while date_start <= date_stop:
            date = date_start.strftime('%Y-%m-%d')
            result = water_db.get_date(date)
            if len(result) == 0:
                lost_list.append(date)
            elif len(result) > 1:
                repeat_dict.update({date: [(item[2],item[3]) for item in result]})

            date_start += timedelta(days=1)

    print('------------------------------------------')
    print(u'*** 数据检查报告 ***')
    print('------------------------------------------')
    print(u' * 数据总数：%d条' % total)
    if date_first and date_last:
        print(u' * 最早日期: %s' % date_first)
        print(u' * 最新日期: %s' % date_last)
    print(u' * 缺失数据：%d条' % len(lost_list))
    for item in lost_list[:15]:
        print(u'   - %s' % item)
    if len(lost_list) > 15:
        print(u'   - ...')
    print(u' * 重复数据：%d天' % len(repeat_dict))
    for date in repeat_dict:
        print(u'   - %s: ' % date)
        for item in repeat_dict[date]:
            try:
                print(u'     > %.02f, %.02f' % (item[0], item[1]))
            except:
                print(date, item)
    print()


def get_plot_data(water_db, start, stop, history):
    """取得绘图数据"""

    # 数据日期范围：start_date ~ stop_date
    total, date_first, date_last = water_db.stat()  # 数据总数、最早数据日期、最新数据日期
    start_date = datetime.strptime(start, '%Y%m%d') if options.start else datetime.strptime(date_first, '%Y-%m-%d')
    stop_date = datetime.strptime(stop, '%Y%m%d') if options.end else datetime.strptime(date_last, '%Y-%m-%d')
    total_days = (stop_date - start_date).days + 1

    # 日期序列：result['date']
    result = dict()
    result.update({'date': [start_date + timedelta(days=i) for i in range(total_days)]})
    result.update({'line': list()})

    # 判断是否包含2月29日
    leap = 0
    for d in result['date']:
        if d.month == 2 and d.day == 29:
            leap = 1

    # 确定是否需要历史同期数据
    if total_days > (365 + leap):  # 日期范围超过一年，则忽略历史同期
        history = 0

    # 以日期序列的年份作为名称
    start_y, stop_y = start_date.year, stop_date.year
    name = '%d' % start_y if start_y == stop_y else '%d-%d' % (start_y, stop_y)

    # 取得数据日期范围内的数据
    d, bt, hh = list(), list(), list()
    for item in water_db.get_data(start_date.strftime('%Y-%m-%d'), stop_date.strftime('%Y-%m-%d')):
        d.append(item[1])
        bt.append(item[2])
        hh.append(item[3])

    # 水位数据对齐日期序列，无数据则补np.nan
    a = [0 for i in range((datetime.strptime(d[0], '%Y-%m-%d') - start_date).days)]
    b = [0 for i in range((stop_date - datetime.strptime(d[-1], '%Y-%m-%d')).days)]
    bt, hh = np.array(a + bt + b), np.array(a + hh + b)
    bt[bt == 0] = np.nan
    hh[hh == 0] = np.nan

    result['line'].append({'name': name, 'bt': bt, 'hh': hh})

    # 取得历史同期数据
    for i in range(history):
        start_y, start_m, start_d = start_date.year - i - 1, start_date.month, start_date.day
        stop_y, stop_m, stop_d = stop_date.year - i - 1, stop_date.month, stop_date.day
        star_str, stop_str = '%d-%02d-%02d' % (start_y, start_m, start_d), '%d-%02d-%02d' % (stop_y, stop_m, stop_d)
        start_d = datetime.strptime(star_str, '%Y-%m-%d')
        stop_d = datetime.strptime(stop_str, '%Y-%m-%d')

        if stop_str < '2012-05-02':
            break

        name = '%d' % start_y if start_y == stop_y else '%d-%d' % (start_y, stop_y)
        days = (stop_d - start_d).days + 1

        d, bt, hh = list(), list(), list()
        for item in water_db.get_data(star_str, stop_str):
            d.append(item[1])
            bt.append(item[2])
            hh.append(item[3])

        if days > total_days:  # 历史同期范围内有2月29日，则需要剔除该日
            leap = False
            for i in range(len(d)):
                if '-02-29' in d[i]:
                    leap = True
                    break
            if leap:
                d.pop(i)
                bt.pop(i)
                hh.pop(i)

        elif days < total_days:  # 日期序列内有2月29日，则历史同期需要在对应位置插入一个nan
            leap = False
            for i in range(1, len(d)):
                if '-03-01' in d[i]:
                    leap = True
                    break
            if leap:
                d.insert(i, '')
                bt.insert(i, 0)
                hh.insert(i, 0)

        y0, m0, d0 = d[0].split('-')
        y1, m1, d1 = d[-1].split('-')

        d0 = datetime.strptime('%d-%s-%s' % (start_date.year, m0, d0), '%Y-%m-%d')
        d1 = datetime.strptime('%d-%s-%s' % (stop_date.year, m1, d1), '%Y-%m-%d')

        a = [0 for i in range((d0 - start_date).days)]
        b = [0 for i in range((stop_date - d1).days)]
        bt, hh = np.array(a + bt + b), np.array(a + hh + b)
        bt[bt == 0] = np.nan
        hh[hh == 0] = np.nan

        result['line'].append({'name': name, 'bt': bt, 'hh': hh})

    return result


def plot(data, mode):
    """绘图"""

    plt.figure('WaterLevel', facecolor='#f4f4f4', figsize=(15, 8))
    plt.title(u'济南地下水位变化曲线图', fontsize=20)
    plt.grid(linestyle=':')
    plt.annotate(u'单位:米', xy=(0, 0), xytext=(0.1, 0.9), xycoords='figure fraction')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(len(data['date']) / 20))

    if len(data['line']) == 1:
        plt.plot(data['date'], data['line'][0]['bt'], color='#ff7f0e', label=u'趵突泉')
        plt.plot(data['date'], data['line'][0]['hh'], color='#2ca02c', label=u'黑虎泉')
    else:
        for item in data['line']:
            if mode:
                plt.plot(data['date'], item['hh'], label=u'黑虎泉（%s）' % item['name'])
            else:
                plt.plot(data['date'], item['bt'], label=u'趵突泉（%s）' % item['name'])

    plt.legend(loc='best')
    plt.gcf().autofmt_xdate()
    plt.show()


def parse_args():
    """获取参数"""

    parser = optparse.OptionParser()

    help = u"检查数据"
    parser.add_option('-v', '--verify', action='store_const', const='verify', dest='cmd', default='verify', help=help)

    help = u"补齐数据"
    parser.add_option('-f', '--fix', action='store_const', const='fix', dest='cmd', help=help)

    help = u"绘制水位线变化图"
    parser.add_option('-p', '--plot', action='store_const', const='plot', dest='cmd', help=help)

    help = u"选择绘图开始日期（格式为YYYYMMDD），默认最早数据日期"
    parser.add_option('-s', '--start', action="store", default=None, help=help)

    help = u"选择绘图结束日期（格式为YYYYMMDD），默认最新数据日期"
    parser.add_option('-e', '--end', action="store", default=None, help=help)

    help = u"设置是否绘制历史同期数据 (参数为数字)，默认不绘制"
    parser.add_option('-H', action="store", dest="history", default=0, help=help)

    help = u"选择趵突泉，默认选择黑虎泉"
    parser.add_option('-b', action="store_false", dest="mode", default=True, help=help)

    return parser.parse_args()


if __name__ == '__main__':

    options, args = parse_args()  # 获取命令和参数
    if options.cmd == 'verify':  # 检查数据
        water_db = WaterDB()
        spring_verify(water_db)
        water_db.close()
    elif options.cmd == 'fix':  # 补齐数据
        water_db = WaterDB()
        deadline = water_db.stat()[2]  # 最新数据日期
        if not deadline:
            deadline ='2012-05-13'
        grab(water_db, deadline)
        spring_verify(water_db)
        water_db.close()
    elif options.cmd == 'plot':  # 数据可视化
        water_db = WaterDB()
        data = get_plot_data(water_db, options.start, options.end, int(options.history))
        plot(data, mode=options.mode)
        water_db.close()