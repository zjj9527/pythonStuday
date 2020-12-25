# 只在表存在时删除
# 如果要删除的表已被删除，或者由于任何其他原因不存在，那么可以使用 IF EXISTS 关键字以避免出错。

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "drop table if exists customers"

mycursor.execute(sql)