# 通配符 %
# where...like...  可以选择以指定字母，短语开头，包含或结束的记录
# 例 ： %way%

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "select * from customers where address like '%way%'"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)