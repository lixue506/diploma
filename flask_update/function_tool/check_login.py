import json
import pymysql
import openpyxl


def login(name, pwd):
    con = pymysql.connect("localhost", "root", "acm506", "zhengshu")
    cur = con.cursor()
    sql = 'select * from admin_info where name = %s and pwd = %s' % ('"'+name+'"', '"'+pwd+'"')
    cur.execute(sql)
    cols = cur.fetchall()
    if cols.count() > 0:
        return True
    return False