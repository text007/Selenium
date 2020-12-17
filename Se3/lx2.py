# 定义函数
def add(a, b):
    print(a + b)
# 调用函数
add(3, 5)
print("------------")

def add(a, b):
    return a + b
c = add(3, 5)
print(c)
print("------------")

# 默认参数与传参
def add(a=1, b=2):
    return a + b
c1 = add()
c2 = add(3, 5)
print(c1)
print(c2)
print("------------")

# 定义 MyClass 类
class MyClass(object):
    def say_hello(self, name):
        return "hello, " + name
# 调用 MyClass 类
mc = MyClass()
print(mc.say_hello("tom"))
print("------------")

# __init__初始化参数
class A:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b
# 调用类时需要传入初始化参数
count = A("4", 5)
print(count.add())

# B 类继承 A 类
class B(A):
    def sub(self, a, b):
        return a - b
print(B(2, 3).add())
