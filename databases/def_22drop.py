# 删除表
# drop table

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"

)

mycursor = mydb.cursor()

sql = "drop table customers"

mycursor.execute(sql)