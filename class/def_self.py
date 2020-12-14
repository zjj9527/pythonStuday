# 1.self参数
# self 参数是对类的当前实例的引用，用于访问属于该类的变量。
# 它不必被命名为 self，您可以随意调用它，但它必须是类中任意函数的首个参数：

class Person():
  def __init__(self,name,age):
    self.name = name
    self.age  = age 

  def myfunc(self):
    print("My name is "+ self.name)

p1  = Person("Bill",26)
p1.myfunc()


# 2.修改属性
# 实例
p1.age = 40

print(p1.age)

# 3.删除对象属性

# del p1.age

print(p1.age) # 会报错

# 4.删除对象

# del p1 
print(p1) # 会报错

