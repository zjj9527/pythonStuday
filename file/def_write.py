# python文件写入

# 如需写入已有的文件，必须向 open() 函数添加参数：
# "a" - 追加 - 会追加到文件的末尾

f = open("test02.txt","a")
f.write("Now the file has more content!")
f.close()

f = open("test02.txt","r")
print(f.read())
f.close()

# "w" - 写入 - 会覆盖任何已有的内容

f = open("test02.txt","w")
f.write("Woops,I have deleted the content!")
f.close()

f = open("test02.txt","r")
print(f.read())
f.close()



# 创建新文件
# 如需在 Python 中创建新文件，请使用 open() 方法，并使用以下参数之一：

# "x" - 创建 - 将创建一个文件，如果文件存在则返回错误
f = open("test03.txt","x")
f.close()
# "a" - 追加 - 如果指定的文件不存在，将创建一个文件
f = open("test04.txt","a")
f.write("Hello,this is test04.txt!")
f.close()
# "w" - 写入 - 如果指定的文件不存在，将创建一个文件
f = open("test05.txt","w")
f.write("Hello,this is test05.txt!")
f.close()