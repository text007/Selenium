# 读取 xml 文件 标签对之间的数据

from xml.dom.minidom import parse

# 打开 xml 文件
dom = parse("./data_file/config.xml")

# 得到文档元素对象
root = dom.documentElement

# 获取（一组）标签
# getElementsByTagName("platform")：获取文件中的标签
tag_name = root.getElementsByTagName("platform")

# firstChild 属性可返回被选节点的第一个子节点，data 表示获取该节点的数据
print(tag_name[0].firstChild.data)
print(tag_name[1].firstChild.data)
print(tag_name[2].firstChild.data)
