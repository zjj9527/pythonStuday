import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"

)

mycursor = mydb.cursor(prepared=True)

mycursor.execute(
  "create table products(id int(40),name varchar(255))"
)

sql = "insert into products(id,name) values (%s,%s)"
val01 =(155,"Tasty Lemons")
val02 = (156,"Vanilla Dreams")
val03 = (154,"chocolate Heaven")

mycursor.execute(sql,val01)
mycursor.execute(sql,val02)
mycursor.execute(sql,val03)

mydb.commit()

mycursor.execute("select * from products")
for x in mycursor:
  print(x)