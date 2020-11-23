# 用filter求素数

# def _odd_iter():
#   n = 1
#   while True:
#     n = n + 2
#     yield n


# def _not_divisible(n):
#   return lambda x: x%n>0

# def primes():
#   yield 2
#   it = _odd_iter()
#   while True:
#     n = next(it)
#     yield n
#     it = filter(_not_divisible(n),it)

# for n in primes():
#   if n <1000:
#     print(n,end=" ")
#   else:
#     break








# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
  # int转换成str   因为int不能直接判断长度
  s1=str(n)
  # 判断长度
  lenth=len(s1)

  for i in range(lenth):
    # 首尾依次递进比较。
    if s1[i] == s1[lenth-i-1]:
      return True
    else:
      return False
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
 