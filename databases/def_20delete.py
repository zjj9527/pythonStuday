# 删除记录
# 使用delete from命令

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "jia9527jia",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "delete from customers where address = 'Mountain 21' "
mycursor.execute(sql)

mydb.commit()  # 删除和插入使用

print(mycursor.rowcount,"record(s) deleted")