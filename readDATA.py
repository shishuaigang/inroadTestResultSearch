# coding=utf-8
import pymssql
import matplotlib.pyplot as plt
import pylab as pl


class readDATA(object):
    def __init__(self, dbname, host, username, password, api_name):
        self.dbname = dbname
        self.host = host
        self.username = username
        self.password = password
        self.sql = api_name

    def read_db(self):
        res_t = []
        conn = pymssql.connect(host=self.host, user=self.username, password=self.password, database=self.dbname)
        cur = conn.cursor()
        print u"连接数据库成功"
        cur.execute(
            "use Inroad_Test_Result select Response_time from Inroad_Crawler_Test where API_URL='" + self.sql + "'")
        for row in cur:
            res_t.append(row[0])
        conn.commit()
        cur.close()
        conn.close()
        return res_t

    def split_url(self):
        Aurl = []
        conn = pymssql.connect(host=self.host, user=self.username, password=self.password, database=self.dbname)
        cur = conn.cursor()
        print u"连接数据库成功"
        cur.execute(
            "use Inroad_Test_Result select distinct API_URL from Inroad_Crawler_Test")
        for row in cur:
            Aurl.append(row[0])
        conn.commit()
        cur.close()
        conn.close()
        return Aurl

    def create_qushitu(self):
        res_list = self.read_db()
        fig, ax = plt.subplots()
        plt.title(self.sql + '  response time')
        plt.ylabel('Response time  (ms)')
        x = [a + 1 for a in range(len(res_list))]
        pl.plot(x, res_list)
        plt.savefig('qushi.png')
