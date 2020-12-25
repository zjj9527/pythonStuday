# 获取已插入行的ID
# 另，如果插入的不止一行，获取的是最后一行

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "insert into customers(name,address) values (%s,%s)"
val = ("Michelle","Blue village")
mycursor.execute(sql,val)

mydb.commit()

print(" 1 record insert:",mycursor.lastrowid) # lastrowid 最后一行的ID