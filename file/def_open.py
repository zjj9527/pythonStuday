# python文件处理

# 文件处理是任何 Web 应用程序的重要组成部分。
# Python 有几个用于1.创建、2.读取、3.更新和4.删除文件的函数。

# 文件处理
# 在 Python 中使用文件的关键函数是 open() 函数。
# open() 函数有两个参数：文件名和模式。
# 有四种打开文件的不同方法（模式）：

# "r" - 读取 - 默认值。打开文件进行读取，如果文件不存在则报错。
# "a" - 追加 - 打开供追加的文件，如果不存在则创建该文件。
# "w" - 写入 - 打开文件进行写入，如果文件不存在则创建该文件。
# "x" - 创建 - 创建指定的文件，如果文件存在则返回错误。
# 此外，您可以指定文件是应该作为二进制还是文本模式进行处理。

# "t" - 文本 - 默认值。文本模式。
# "b" - 二进制 - 二进制模式（例如图像）。

f = open("test.txt")

f.close()

