# 主键

import mysql.connector

mydb  = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("create table customers (id int auto_increment,name varchar(255),address   varchar(255) )")