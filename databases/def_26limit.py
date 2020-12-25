# 从另一个位置开始
# offset

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "select * from customers limit 5 offset 2 "
mycursor.execute(sql)

myresult = mycursor.fetchall()


for x in myresult:
  print(x)