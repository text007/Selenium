# 异常
# FileNotFoundError 试图打开一个不存在的文件或目录
# open("abc.txt", "r")

try:
    open("abc.txt", "r")
except FileNotFoundError:
    print("异常了")
print("------------")

# NameError 使用一个还未赋值对象的变量
try:
    print(a)
except NameError:
    print("异常了")
print("------------")

# BaseException 新的所有异常类的基类
try:
    open("abc.txt", "r")
    print(a)
except BaseException as msg:
    print(msg)
print("------------")

try:
     a = "异常测试"
     print(a)
except NameError as msg:
    print(msg)
else:
    print("没有异常时执行！")
print("------------")

try:
    # b = "异常测试"
    print(b)
except NameError as msg:
    print(msg)
finally:
    print("不管是否出行异常，都会被执行")
print("------------")

# 抛出异常
def say_hello(name=None):
    if name is None:
        raise NameError("name cannot be empty")
    else:
        print("hell, %s" % name)

say_hello(1)
