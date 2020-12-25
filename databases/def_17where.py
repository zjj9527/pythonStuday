# 防sql注入
# 当用户提供查询值时，您应该转义这些值。
# 此举是为了防止 SQL 注入，这是一种常见的网络黑客技术，可以破坏或滥用您的数据库。
# mysql.connector 模块拥有转义查询值的方法

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "select * from customers where address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql,adr)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)