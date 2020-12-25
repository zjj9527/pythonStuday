import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"

)

mycursor = mydb.cursor()

sql = "insert into users(id,name) values (%s,%s)"
val = (5,"Michael")
mycursor.execute(sql,val)
mydb.commit()

mycursor.execute("select * from users")

for x in mycursor:
  print(x)