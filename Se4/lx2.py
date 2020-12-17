# 浏览器前进后台操作
from selenium import webdriver
import time

driver = webdriver.Firefox()

# 访问百度首页
first_url = "http://www.baidu.com"
print("now access %s" % first_url)
driver.get(first_url)

# 访问新闻页
time.sleep(2)   # 暂停2秒
second_url = "http://news.baidu.com"
print("now access %s" % second_url)
driver.get(second_url)

# 返回（后退） 到百度首页
time.sleep(2)
print("back to %s" % first_url)
driver.back()   # 返回（后退）一步

# 前进到新闻页
time.sleep(2)
print("forward to %s" % second_url)
driver.forward()    # 前进一步
