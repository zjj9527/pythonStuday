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




# 测试
x = datetime.datetime.now()
print(x.strftime("%a"))  #  weekday 短版本  Wed
print(x.strftime("%A"))  #  weekday 完整版本 Wednesday
print(x.strftime("%w"))  #  Weekday，数字 0-6，0 为周日    1
print(x.strftime("%d"))  #  日，数字01-31   14 
print(x.strftime("%b"))  #  月，短版本    Dec
print(x.strftime("%B"))  #  月，完整版本  December
print(x.strftime("%m"))  #  月, 数字01-12，12
print(x.strftime("%a"))  #  年，短版本，无世纪  20
print(x.strftime("%A"))  #  年， 完整版本，   2020
print(x.strftime("%H"))  #  小时，00-23     16
print(x.strftime("%I"))  #  小时，00-12     04
print(x.strftime("%p"))  #  AM/PM     PM
print(x.strftime("%M"))  #  分 00-59  59
print(x.strftime("%S"))  #  秒 00-59  55
print(x.strftime("%j"))  #  天数  001-365  300
print(x.strftime("%c"))  #  日期和时间的本地版本  Mon Dec 14 17:01:40 2020
print(x.strftime("%x"))  #  日期的本地版本  12/14/20
print(x.strftime("%X"))  #  时间的本地版本  17:03:25


