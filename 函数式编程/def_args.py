# 使用generator及next()生成一个计数器
def createCounter():
  def iterator():  # 定义一个生成器，逐个生成1,2,3...的数列
    n = 0
    while True:
      n = n + 1
      yield n 
  it = iterator() # 声明一个变量it，指向生成器
  def counter():
    return next(it)
  return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
