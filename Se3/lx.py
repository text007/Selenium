# 打印
print("hello pytest")
print("------------")

# 格式化输出
name = "tom"
age = 27
print("name is : " + name + ". age is: " + str(age))
print("------------")

print("name is : %s, age is: %d" % (name, age))
print("------------")

print("name is : {}, age is: {}".format(name, age))
print("------------")

print("name is: {1}, age is: {0}".format(age, name))
print("name is: {n}, age is: {a}".format(n=name, a=age))
print("------------")
