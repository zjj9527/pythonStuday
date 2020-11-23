# 用sorted()排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 定义一个转换函数
def by_name(t):
    print (t[0])
    return t[0]

def by_score(t):
    print(t[1])
    return (-t[1])

# 测试
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score)
print(L3)