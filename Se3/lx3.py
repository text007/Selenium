# 调用 time 模块
import time
# 直接导入 time 模块下的多个函数
from time import ctime, sleep
# 导入 time 模块下的所有函数
# from time import *
# 对导入的 sleep 函数重命名
from time import sleep as sys_sleep
print(time.ctime())
sleep(2)
print(ctime())

