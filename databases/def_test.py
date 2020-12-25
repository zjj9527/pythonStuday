import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"

)

mycursor = mydb.cursor()

mycursor.execute("drop table if exists products")

mycursor.execute("show tables")

for x in mycursor:
  print(x)