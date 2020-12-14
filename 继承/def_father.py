# Python 继承
# 继承允许我们定义继承另一个类的所有方法和属性的类。
# 父类是继承的类，也称为基类。
# 子类是从另一个类继承的类，也称为派生类。

# 1.创建父类
# 任何类都可以是父类，因此语法与创建任何其他类相同：
class Person:
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname,self.lastname)

p1 = Person("Bill","Gates")
p1.printname()

# 2. 创建子类
# 要创建从其他类继承功能的类，请在创建子类时将父类作为参数发送：
class Student(Person):
  pass
# 如果您不想向该类添加任何其他属性或方法，请使用 pass 关键字。

s1 = Student("Elon","Musk")
s1.printname()


# 3.添加__init__()方法
# 每次使用类创建新对象时，都会自动调用 __init__() 函数。

# 调用super()函数
# 添加属性
class Students(Person):
  def __init__(self,fname,lname,year):
    super().__init__(fname,lname)   # 或者使用 Person.__init__(self,fname,lname)
    self.graduationyear = year
  # 添加方法
  def welcome(self):
    print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)



x = Students("Elon","Musk",2019)
x.welcome()