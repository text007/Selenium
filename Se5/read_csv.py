# 读取 csv 文件

import csv
import codecs
from itertools import islice

# 读取本地 csv 文件
# codecs:是 Python 标准的模块编码和解码器
# reader()方法读取文件
data = csv.reader(codecs.open("./data_file/user_info.csv", "r", "gbk"))

# 存放用户数据
users = []

# 循环输出每行信息
# islice(data, 1, None):返回一个迭代器，第一个参数指定迭代对象，第二个参数指定开始迭代的位置，第三个参数表示结束位。
for line in islice(data, 1, None):
    users.append(line)

# 打印
print(users)
