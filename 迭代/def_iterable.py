# 创建迭代器
# 要把对象/类创建为迭代器，必须为对象实现 __iter__() 和 __next__() 方法。
# 正如您在 Python 类/对象 一章中学到的，所有类都有名为 __init__() 的函数，它允许您在创建对象时进行一些初始化。
# __iter__() 方法的作用相似，您可以执行操作（初始化等），但必须始终返回迭代器对象本身。
# __next__() 方法也允许您执行操作，并且必须返回序列中的下一个项目。
# StopIteration
# 如果你有足够的 next() 语句，或者在 for 循环中使用，则上面的例子将永远进行下去。
# 为了防止迭代永远进行，我们可以使用 StopIteration 语句。
# 在 __next__() 方法中，如果迭代完成指定的次数，我们可以添加一个终止条件来引发错误

# 实例

class Numbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a +=1
      return x

    else:
      raise StopIteration
  

myclass = Numbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
