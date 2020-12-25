# 选取列，只选取其中的一部分，后跟列名

# 仅仅选取了名称和地址列
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("select name,address from customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)