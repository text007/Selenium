# 表单提交（搜索内容的提交）
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

search_test = driver.find_element_by_id("kw") # 定位元素
time.sleep(2) # 暂停2秒
search_test.send_keys("selenium") # 模拟按键输入
time.sleep(2) # 暂停2秒
search_test.submit() # 表单提交（通过按键盘上的回车键完成搜索内容的提交）

driver.quit() # 关闭浏览器
