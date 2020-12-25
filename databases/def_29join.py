# right join   返回右边的对照
# 如果您想要返回所有产品以及喜欢它们的用户，即使没有用户喜欢这些产品，请使用 RIGHT JOIN 语句
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="jia9527jia",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  right JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)