import pymysql

user = input("name:")
pwd = input("password:")

conn = pymysql.connect(host="127.0.0.1",user='root',password='Haoxiaoyu7!',database="db1")
cursor = conn.cursor()
sql = "select * from user where name=%s and password=%s"

print(sql)
cursor.execute(sql,[user,pwd])

#通过字符串
result = cursor.fetchone()
print(result)
