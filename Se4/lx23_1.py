from selenium import webdriver
import time
from selenium.webdriver import TouchActions
driver = webdriver.Firefox()
driver.get('https://www.jq22.com/yanshi3714')
time.sleep(2)
driver.switch_to.frame("iframe")
driver.find_element_by_xpath('//*[@id="text"]').click()
list = driver.find_elements_by_xpath('//*[@class="dwwo"]')
year = list[0]
month = list[1]
day = list[2]
a = TouchActions(driver)
# 滑动月
a.scroll_from_element(month, 0, -8).perform()
# 滑动日
a.scroll_from_element(day, 0, 8).perform()
# 滑动年
a.scroll_from_element(month, 0, 8).perform()
