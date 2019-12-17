import os
import sqlite3


class WaterDB:
    """水位数据库"""

    def __init__(self):
        """构造函数"""

        fn_db = 'spring.db'
        is_db = os.path.exists(fn_db)

        self._conn = sqlite3.connect(fn_db)
        self._cur = self._conn.cursor()
        if not is_db:
            self._create_table()

    def _create_table(self):
        """创建表spring，共3个字段：date(日期)、bt(趵突泉水位)、hh(黑虎泉水位)"""

        sql = '''CREATE TABLE spring(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE,
                bt REAL,
                hh REAL
              )'''

        self._execute(sql)
        self._conn.commit()

    def _execute(self, sql, args=()):
        """运行SQ语句"""

        if isinstance(args, list):  # 批量执行SQL语句，此时parameter是list，其元素是tuple
            self._cur.executemany(sql, args)
        else:  # 单次执行SQL语句，此时parameter是tuple或者None
            self._cur.execute(sql, args)

        if sql.split()[0].upper() != 'SELECT':  # 非select语句，则自动执行commit()
            self._conn.commit()

        return self._cur.fetchall()

    def close(self):
        """关闭数据库连接"""

        self._cur.close()
        self._conn.close()

    def append(self, data):
        """插入水位数据"""

        sql = 'INSERT INTO spring (date, bt, hh) values (?, ?, ?)'
        self._execute(sql, data)

    def dedup(self):
        """去除各个字段完全重复的数据，只保留id最小的记录"""

        self._execute('delete from spring where id not in(select min(id) from spring group by date, bt, hh)')

    def rectify(self, err_list):
        """更新已知的日期错误"""

        for item in err_list:
            if item[3]:
                sql = 'update spring set date=? where date=? and bt=? and hh=?'
                self._execute(sql, (item[3], item[0], item[1], item[2]))
            else:
                sql = 'delete from spring where date=? and bt=? and hh=?'
                self._execute(sql, (item[0], item[1], item[2]))

    def fill(self, missing_list):
        """补缺"""

        for item in missing_list:
            res = self._execute('select * from spring where date=? and bt=? and hh=?', (item[0], item[1], item[2]))
            if not res:
                sql = 'insert into spring (date, bt, hh) values (?, ?, ?)'
                self._execute(sql, item)

    def stat(self):
        """统计信息：数据总数、最早数据日期、最新数据日期"""

        total = 0
        date_first = None
        date_last = None

        res = self._execute('select date from spring order by date')
        if res:
            total = len(res)
            date_first = res[0][0]
            date_last = res[-1][0]

        return total, date_first, date_last

    def get_data(self, date1, date2=None):
        """取得指定日期或日期范围的水位数据"""

        if date2:
            return self._execute('select * from spring where date>=? and date<=? order by date', (date1, date2))
        else:
            return self._execute('select * from spring where date= ?', (date1,))


if __name__ == '__main__':
    pass
