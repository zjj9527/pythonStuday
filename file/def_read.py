# 在服务器上打开文件
f = open("test.txt")
print(f.read())
f.close()

# 只读取文件的一部分
f = open("test.txt")
print(f.read(5))
f.close()

# 读行   可以使用readline()方法返回一行
f = open("test.txt")
print(f.readline())
f.close()

# 通过循环遍历文件中所有的行，可以读取整个文件
f = open("test.txt")
for i in f:
  print(i)

# 关闭文件
f = open("test.txt")
f.close()