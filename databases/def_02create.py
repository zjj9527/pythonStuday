# 创建数据库

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia"
)

mycursor = mydb.cursor()
mycursor.execute("create database mydatabase")