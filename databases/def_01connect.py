# 创建连接
import mysql.connector

mydb = mysql.connector.connect(

  host = "localhost",
  user = "root",
  passwd = "jia9527jia"
)
print(mydb)