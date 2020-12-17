# 读取 json 文件

import json

with open("./data_file/user_info.json", "r") as f:
    adta = f.read()

user_list = json.loads(adta)
print(user_list)
