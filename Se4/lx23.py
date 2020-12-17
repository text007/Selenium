# 上下滑动选择日期

from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.jq22.com/yanshi4976")
sleep(2)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

# 定位要滑动的年、月、日
dwwos = driver.find_elements_by_class_name("dwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

# 滑动元素
action = webdriver.TouchActions(driver)
action.scroll_from_element(year, 0, 5).perform()
action.scroll_from_element(month, 0, 30).perform()
action.scroll_from_element(day, 0, 30).perform()


"""
这里使用 TouchActions 类中的 scroll_from_element()方法滑动元素，参数如下。
 on_element：滑动的元素。
 xoffset：x 坐标距离。
 yoffset：y 坐标距离。
"""
