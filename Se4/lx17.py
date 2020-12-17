# 上传文件

import os
from selenium import webdriver

# 获取当前路径的 “files” 文件夹
file_path = os.path.abspath("./files//")

# 浏览器打开文件夹的 upfile.html 文件
driver = webdriver.Firefox()
upload_page = "file:///" + file_path + "/upfile.html"
driver.get(upload_page)

# 定位上传按钮，添加本地文件
driver.find_element_by_id("inputfile").send_keys(file_path + "\\test.txt")
