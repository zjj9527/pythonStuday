# 递归函数
def fact(n):
  if n==1:
    return 1
  return n*fact(n-1)