# 使用筛选器来选取
# 从表中选取记录时，可以使用where语句进行筛选

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"

)

mycursor = mydb.cursor()

sql = "select * from customers where address ='Park Lane 38'"
mycursor.execute(sql)

myresult  = mycursor.fetchall()
for x in myresult:
  print(x)