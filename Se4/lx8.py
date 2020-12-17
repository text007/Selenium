# 获得验证信息

from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
print("Before search===============")

# 打印当前页面 title
sleep(2)
title = driver.title
print("title:" + title)

# 打印当前页面url
sleep(2)
now_url = driver.current_url
print("URL:" + now_url)

sleep(2)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

print("After search===============")

# 再次打印当前页面title
sleep(2)
title = driver.title
print("title:" + title)

# 再次打印当前页面url
sleep(2)
now_url = driver.current_url
print("URL:" + now_url)

# 获取搜索结果条数
sleep(2)
num = driver.find_element_by_class_name("nums").text
print("result:" + num)

driver.quit()

"""
title：用于获取当前页面的标题。
current_url：用于获取当前页面的 URL。 
text：用于获取当前页面的文本信息。(搜索结果条目数)
"""