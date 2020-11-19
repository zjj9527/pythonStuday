# 请定义一个函数quadratic(a, b, c),
# 接收3个参数,
# 返回一元二次方程 ax^2+bx+c=0的两个解。

import math 
def quadratic(a,b,c):
  m = b*b - a*c*4
  if m>0:
    x = (-b + math.sqrt(m))/(2*a)
    y = (-b - math.sqrt(m))/(2*a)
    return x, y
  else:
    return "No Answer!"
print("quadratic(2,3,1)=",quadratic(2,3,1))
print("quadratic(1,3,-4)=",quadratic(1,3,-4))

if quadratic(2,3,1) != (-0.5,-1.0):
  print("测试失败！")
elif quadratic(1,3,-4) != (1.0,-4.0):
  print("测试失败！")
else:
  print("测试成功！")
  