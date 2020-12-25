# left join  返回左边的对照
# 如果希望显示所有用户，即使他们没有喜欢的产品，请使用 LEFT JOIN 语句：
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
  LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)