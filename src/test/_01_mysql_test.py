
import pymysql;

#连接mysql
db = pymysql.connect(host='192.168.222.111', port=3306, user='root', passwd='123456', db='school', charset='utf8')
cursor = db.cursor()

#查询数据库版本
cursor.execute("select version()")
data = cursor.fetchone()
print(" Database Version:%s" % data)

#查询表
sql = "select * from student"
cursor.execute(sql)
data = cursor.fetchone()
print(data)