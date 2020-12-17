import sys
from os.path import dirname, abspath
# 得到当前目录上级目录决定路径
project_path = dirname(dirname(abspath(__file__)))
# 得到当前目录上上级目录决定路径
project_path1 = dirname(dirname(dirname(abspath(__file__))))
print(project_path)
print(project_path1)
# 路径拼接
sys.path.append(project_path + "\\module")
from calculator import add

# 调用add（）函数
c = add(2, 3)
print(c)
