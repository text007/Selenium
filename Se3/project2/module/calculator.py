# 创建 add()函数
def add(a, b):
    return a + b

# “if __name__ == '__main__':”表示当模块被直接运行时，下面的代码块将被运行；
# 当模块被其他程序文件调用时，下面的代码块不被运行。
if __name__ == "__main__":
    c = add(3, 5)
    print(c)
