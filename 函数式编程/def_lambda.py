# lambda 函数是一种小的匿名函数。
# lambda 函数可接受任意数量的参数，但只能有一个表达式。
# 语法
# lambda arguments : expression

def myfunc(n):
  return lambda a : a**n

mydoubler = myfunc(2)

print(mydoubler(3))