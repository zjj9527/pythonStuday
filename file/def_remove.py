# python删除文件
# 如需删除文件，必须导入 OS 模块，并运行其 os.remove() 函数：

# 例
import os
os.remove("test03.txt")

# 检查文件是否存在
if os.path.exists("test05.txt"):
  os.remove("test05.txt")
else:
  print("The file don't exist!")

# 删除整个文件夹
# 如需删除整个文件夹，请使用 os.rmdir() 方法：

os.rmdir("test")