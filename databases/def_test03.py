import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"

)

mycursor = mydb.cursor(prepared=True)

mycursor.execute(
  "create table users(id int(100),name varchar(255) ,fav int(200) )"
)

sql = "insert into users (id,name,fav) values (%s,%s,%s)"
val = [
  (1,"John",154),
  (2,"Peter",154),
  (3,"Amy",155),
  # (4,"Hannah",),
  # (5,"Michael",)
]
mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)