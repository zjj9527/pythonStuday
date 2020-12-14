# 对象方法
# 对象也可以包含方法，对象中的方法就是属于该对象的函数

class Person():
  def __init__(self,name,age):
    self.name =name
    self.age  = age
  def myfunc(self):
    print("My name is "+self.name)

p1 = Person("Bill",26)
p1.myfunc()

# 提示：self 参数是对类的当前实例的引用，用于访问属于该类的变量。