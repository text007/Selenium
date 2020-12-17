# if 语句
a = 2
b = 3

if a > b:
    print("a max!")
else:
    print("b max!")
print("------------")

# if 语句，判断运算符是否等于（==）
if 2 + 2 == 4:
    print("true")
else:
    print("false")
print("------------")

# if 语句，判断运算符是否在（in）
s = "hello"
ss = "hello world"
if s in ss:
    print("contain")
else:
    print("not contain")
print("------------")

# if 语句，判断运算符是否（true，false）
if True:
    print("true")
else:
    print("false")
print("------------")

# if 语句，多重判断
result = 72
if result >= 90:
    print("优先")
elif result >= 70:
    print("良好")
elif result >= 60:
    print("及格")
else:
    print("不及格")
print("------------")

# for 循环语句
# 循环遍历字符串
for s in "hello":
    print(s)
print("------------")

# 循环遍历列表
fruits = ["banana", "apple", "mango"]

for fruit in fruits:
    print(fruit)
print("------------")

# 循环遍历 5 次
for i in range(5):
    print(i)
print("------------")

# 打印 1~10 之间的奇数
for i in range(1, 10, 2):
    print(i)
print("------------")

# 定义列表
lists = [1, 2, 3, "a", 5]
# 打印列表
print(lists)
# 打印列表中的第 1 个元素
print(lists[0])
# 打印列表中的第 5 个元素
print(lists[4])
# 打印列表中的最后一个元素
print(lists[-1])

# 修改列表中的第 5 个元素为“b”
lists[4] = "b"
print(lists)

# 在列表末尾添加元素
lists.append("c")
print(lists)

# 删除列表中的第一个元素
lists.pop(0)
print(lists)
print("------------")

# 元组
# 定义元组
tup1 = ("a", "b", 3, 4)
tup2 = (1, 2, 3)

print(tup1[0])
print(tup2[0:2])

# 连接元组
tup3 = tup1 + tup2
print(tup3)

#复制元组
tup4 = ("hi!")
print(tup4 * 3)
print("------------")

dicts = {"username": "zhangsan", "password": 123456}
# 打印字典中的所有 key
print(dicts.keys())
# 打印字典中的所有 value
print(dicts.values())

# 向字典中添加键/值对
dicts["age"] = 22

# 循环打印字典 key 和 value
for k, v in dicts.items():
    print("dicts keys is %r" % k)
    print("dicts values is %r" % v)

# 删除键是'password'的项
dicts.pop("password")

# 打印字典以列表方法返回
print(dicts.items())
