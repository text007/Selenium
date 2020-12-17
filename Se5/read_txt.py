# 读取txt文件

# readlines():读取文件所有内容
with(open("./data_file/user_info.txt", "r")) as user_file:
    data = user_file.readlines()

# 格式化处理
# [:-1]：去掉最后一个元素
# split(":")：每行数据以 : 进行拆分
users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)

# 打印 users 二维数组
print(users)
