# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# 思路 


# 导入模块
from functools import reduce


# 定义一个实现功能的函数
def str2float(s):

  # 写一个字典，可以和数值对应
  def char2num(s):
    digits={
      "0":0,
      "1":1,
      "2":2,
      "3":3,
      "4":4,
      "5":5,
      "6":6,
      "7":7,
      "8":8,
      "9":9,
    }
    return digits[s]
  
  # 判断有没有小数点
  # 有
  if '.' in s:
    # 将“.”前后分离
    l=s.split(".",2)
    # 各用一个集合接收
    L1=list(map(char2num,l[0]))
    L2=list(map(char2num,l[1]))
    # 还原顺序
    s1=reduce(lambda x,y: x*10+y,L1)
    s2=reduce(lambda x,y: x*10+y,L2)
    # 组合
    lenth=len(L2)
    a = s1+s2/(10**lenth)
    return a
  # 没有
  else:
    a = reduce(lambda x,y: x*10+y,map(char2num,s))
    return a


print(str2float('123.456'))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')