# 检查数据库是否存在

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia"
)
mycursor = mydb.cursor()

mycursor.execute("show databases")

for x in mycursor:
  print(x)