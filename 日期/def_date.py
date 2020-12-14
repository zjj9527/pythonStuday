# 导入日期模块
import datetime

# 现在时间
x = datetime.datetime.now()
print(x)
# 返回 weekday 的名称和年份：
print(x.year)
print(x.strftime("%A"))

# 创建日期对象
# 如需创建日期，我们可以使用 datetime 模块的 datetime() 类（构造函数）。
# datetime() 类需要三个参数来创建日期：年、月、日。
x = datetime.datetime(2020,5,20)
print(x)
# datetime() 类还接受时间和时区（小时、分钟、秒、微秒、tzone）的参数，不过它们是可选的，默认值为 0，（时区默认为 None）。

# strftime()方法。
# datetime 对象拥有把日期对象格式化为可读字符串的方法。
# 该方法称为 strftime()，并使用一个 format 参数来指定返回字符串的格式：

x = datetime.datetime(2019,10,1)
print(x.strftime("%B"))
