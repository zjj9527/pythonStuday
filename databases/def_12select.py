# 从表中选取所用数据

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("select * from customers")

myresult = mycursor.fetchall()  #fetchall() 方法，该方法从最后执行的语句中获取所有行。

for x in myresult:
  print(x)
