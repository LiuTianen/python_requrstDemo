#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
# print(time.time())    #返回当前时间的时间戳

# start = time.perf_counter() #记录启动时间
# time.sleep(random.random()) #在【0，1）秒中范围内随机休眠，模拟代码的运行
# end = time.perf_counter()   #记录结束时间
# print(end- start)   #打印代码的运行时长

# print(time.localtime())
# #将时间戳转换成本地时区的struct_time类。不提供时间戳，则使用当前时间戳
# print(time.gmtime())
# #将时间戳转换成零时区的struct_time类。不提供时间戳，则使用当前时间戳
# print(time.localtime(0))
# #0时间戳，对应东8区，就是1970-1-1：8时
# print(time.gmtime(0))
# #0时间戳，对应格林尼治时间零时区，就是1970-1-1：0时
# print(time.mktime(time.localtime()))
# #struct_time类转时间戳


# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# #将当前日期时间转换成YYYY-MM-DD hh:mm:ss 的格式
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1573280000)))
# #将时间戳转成 YYYY-MM-DD hh:mm:ss 的格式
# print(time.mktime(time.strptime('2019-10-28 08:00:00', '%Y-%m-%d %H:%M:%S')))
# #将时间日期字符串转成时间戳


print(time.asctime())
#返回当前时间的时间字符串
print(time.asctime((2019, 10, 1, 12, 30, 30, 0, 0, 0)))
#将时间元组转为时间字符串
print(time.ctime())
#将时间戳转换成替父传，默认当前时间的时间戳
print(time.process_time())
#使用CPU的时长（秒）