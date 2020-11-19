# 关键字参数
# 参数是字典
def person(name,age,**kw):
  print("name:",name,"age:",age,"other:",kw)

# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 如果已经有一个dict,可以直接使用
exter={"city":"ShangCai","job":"Engineer"}
person("LeMing",20,**exter)


# 命名关键字参数
def person01(name,age,*,city,job):
  print(name,age,city,job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person("jiajia",25,city="BeiJing",job="Engineer")

# 命名关键字参数必须传入参数名，这和位置参数不同。
# 如果没有传入参数名，调用将报错：
# 参数名： city  job
