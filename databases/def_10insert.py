# 插入表，单行 使用insert into语句

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase" 
)

mycursor = mydb.cursor()

sql = "insert into customers(name,address) values (%s,%s)"
val = ("John","Highway 21")
mycursor.execute(sql,val)  # 添加进表
mydb.commit()  # 重点  必须使用

print(mycursor.rowcount,"record insert")