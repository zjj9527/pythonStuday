# 表已经存在 使用alter table关键字

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("alter table customers add column id int auto_increment primary key")