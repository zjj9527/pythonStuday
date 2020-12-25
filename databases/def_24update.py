# 更新表
# update ....  set .....

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "update customers set address= %s where address= %s"
val =("Valley 345", "Canyon 123")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record(s) affectd")