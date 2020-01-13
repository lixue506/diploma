'''
数据库操作
'''
import pymysql
import base64
class Operator_mysql():

    #修改密码
    def Change_pwd(self, name, pwd):
        try:
            con = pymysql.connect("localhost", "root", "lixue123", "test")
            cur = con.cursor()
            sql = "update user set pwd={} where name={}".format(pwd, name)
            cur.execute(sql)
            con.commit()
            con.close()  # 本地运行，我也不知道用不用关闭数据库，但是不碍事
            return 1
        except:
            return 0
    # 注册账号
    def Register(self, name, pwd):
        try:
            con = pymysql.connect("localhost", "root", "lixue123", "test")
            cur = con.cursor()
            sql = "insert into user values({},{})".format(pwd, name)
            cur.execute(sql)
            con.commit()
            con.close()
            return 1
        except:
            return 0
    # 登陆判断
    def Login_Judge(self, name,pwd):
        try:
            con = pymysql.connect("localhost", "root", "lixue123", "test")
            cur = con.cursor()
            sql = "select * from user where name={} and pwd={}".format(name, pwd)
            cur.execute(sql)
            cols = cur.fetchall()
            con.close()
            return 1 if len(cols) > 0 else 0
        except:
            return 0
    # 数据查询
    def Query(self, kind, q):
        try:
            con = pymysql.connect("localhost", "root", "lixue123", "test")
            cur = con.cursor()
            sql = "select * from user where {}={}".format(kind, q)
            cur.execute(sql)
            cols = cur.fetchall()
            con.close()
            return self.form_data(cols)
        except:
            return 0
    # 格式化数据
    def form_data(self, cols):
        mysql_data_dict = {}
        for index_ in range(len(cols)):
            for i in cols[index_]:
                d = {}
                d['Id'] = i[0]  # 证书编号
                d['User'] = i[1]              # 学号 持有者
                d['Times'] = i[2]               # 获得日期
                d['Show'] = 'Show'             # 查看
                d['Download'] = 'Download'      # 下载
                mysql_data_dict[index_+1] = d
        return mysql_data_dict

