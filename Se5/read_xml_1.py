# 读取 xml 文件 标签的属性值

from xml.dom.minidom import parse

dom = parse("./data_file/config.xml")
# 得到文档元素对象
root = dom.documentElement

# 获取（一组）标签
login_info = root.getElementsByTagName("login")

# 获取login 标签的 password 属性值
username = login_info[0].getAttribute("username")
print(username)

password = login_info[0].getAttribute("password")
print(password)

username = login_info[1].getAttribute("username")
print(username)

password = login_info[1].getAttribute("password")
print(password)
