# 要理解类的含义，我们必须先了解内置的 __init__() 函数。
# 所有类都有一个名为 __init__() 的函数，它始终在启动类时执行。
# 使用 __init__() 函数将值赋给对象属性，或者在创建对象时需要执行的其他操作：

class Person():
  def __init__(self,name,age):
    self.name = name
    self.age = age

p1 = Person("Bill",26)

print(p1.name)
print(p1.age)

# 注释：每次使用类创建新对象时，都会自动调用 __init__() 函数。