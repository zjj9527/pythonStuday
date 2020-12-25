# 降序排列 使用desc关键字

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "select * from customers order by name desc"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)