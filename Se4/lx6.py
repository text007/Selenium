# 鼠标操作

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.cn")

# 定位到要悬停的元素
above = driver.find_element_by_id("s-usersetting-top")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

"""
ActionChains(driver)
    调用 ActionChains 类，把浏览器驱动 driver 作为参数传入。
move_to_element(above)
    move_to_element()方法用于模拟鼠标移动到元素上，在调用时需要指定元素。
perform()
    提交所有 ActionChains 类中存储的行为。
"""
