import pymysql

user = input("name:")
pwd = input("password:")

conn = pymysql.connect(host="127.0.0.1",user='root',password='Haoxiaoyu7!',database="db1")
cursor = conn.cursor()

"""
第一种方法

sql = "insert into user(name,password) values(%s,%s)"
cursor.execute(sql,[user,pwd])
"""

"""
第二种方法

sql = "insert into user(name,password) values('%s','%s')" %(user,pwd);
cursor.execute(sql)
"""


"""
清空表数据

sql = "truncate table user"
cursor.execute(sql)
conn.commit()
conn.close()
"""
