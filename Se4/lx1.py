# 设置浏览器窗口大小
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://m.baidu.com")

print("设置浏览器宽480，高800 显示")
driver.set_window_size(480, 800)
driver.quit()
