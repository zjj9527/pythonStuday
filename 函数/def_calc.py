#可变参数
# list 或者 tuple 参数
def calc(numbers):
  sum = 0 
  for  n  in numbers:
    sum = sum + n * n
  return sum 



# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def calc02(*numbers):
  sum = 0 
  for  n  in numbers:
    sum = sum + n * n
  return sum 


b = calc02(1,5,3,7)
print(b)
c = calc02(1,2,3)
print(c)

# 如果已经有一个list或者tuple参数，可以允许在list或者tuple前面加一个*
num = [1,2,3]
a = calc02(*num)
print(a)