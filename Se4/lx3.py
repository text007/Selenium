# 浏览器输入搜索操作
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

time.sleep(2)
driver.find_element_by_id("kw").clear() # 清除文本
time.sleep(2)
driver.find_element_by_id("kw").send_keys("selenium") # 模拟按键输入
time.sleep(2)
driver.find_element_by_id("su").click() # 点击元素
driver.quit() # 关闭浏览器
