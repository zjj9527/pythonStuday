import mymodule 
import platform as pf  # 用as为模块重命名
mymodule.greeting("Bill")

# 注释：如果使用模块中的函数时，请使用以下语法：
# module_name.function_name

a = mymodule.person1["age"]
print(a)

x = pf.system()
print(x)

# 使用 dir() 函数
# 有一个内置函数可以列出模块中的所有函数名（或变量名）。dir() 函数：

y = dir(pf)
print(y)

# ------****------
# 重点
from mymodule import person1
print (person1["age"])
# 提示：在使用 from 关键字导入时，请勿在引用模块中的元素时使用模块名称。示例：person1["age"]，而不是 mymodule.person1["age"]。