# 防止 SQL 注入
# 在 delete 语句中，转义任何查询的值也是一种好习惯。
# 此举是为了防止 SQL 注入，这是一种常见的网络黑客技术，可以破坏或滥用您的数据库。
# mysql.connector 模块使用占位符 ％s 来转义 delete 语句中的值：

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "delete from customers where address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql,adr)

mydb.commit()

print(mycursor.rowcount,"record(s) deleted")

