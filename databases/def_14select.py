# fetchone()   只获取一行

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("select * from customers")

myresult = mycursor.fetchone() # 只取上面的第一条结果，反复使用，依次获得下一条结果

print(myresult)
