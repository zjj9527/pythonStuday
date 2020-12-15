
# JSON 是用于存储和交换数据的语法。
# JSON 是用 JavaScript 对象表示法（JavaScript object notation）编写的文本



import json
# 1. json.loads()  解析json---把json转换为python    -----结果是字典
# json x
x = '{"name":"Bill","age":63,"city":"Seatle"}'
# 解析 x 
y = json.loads(x)

print(y)


# 2. json.dumps()   把python转换为python
x = {"name":"Bill",
      "age":63,
      "city":"Seatle"}
# x 转换为python
y = json.dumps(x)

print(y)


# 3.当 Python 转换为 JSON 时，Python 对象会被转换为 JSON（JavaScript）等效项
x = {
  "name":"Bill",
  "age":26,
  "city":"Seatle",
  "married":True,
  "divorced":False,
  "children":("Jennifer","Rory","Phoebe"),
  "pets":None,
  "cars":[
    {"model":"Porsche","mpg":38.2},
    {"model":"BMW M5", "mpg":26.9}
  ]
}
print(json.dumps(x))


# 4 格式化结果
# 使用indent参数定义缩进数
print(json.dumps(x,indent=4))

# 使用separators参数更改默认的分隔符
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# 对结果排序
# 使用 sort_keys 参数来指定是否应对结果进行排序：
print(json.dumps(x,indent=4,separators=(".","="),sort_keys=True))
