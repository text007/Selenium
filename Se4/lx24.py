# 窗口截图

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 截取当前窗口，指定截图图片的保存位置
driver.save_screenshot("./files/baidu_img.png")
