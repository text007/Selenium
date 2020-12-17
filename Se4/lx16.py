# 下拉框处理

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# 打开搜索设置
link = driver.find_element_by_id("s-usersetting-top").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(3)

# 搜索结果显示条数
sel = driver.find_elements_by_xpath("//select[@id='nr']")

# value="20"
Select(sel).select_by_value("20")
sleep(3)

# <option>每页显示50条《/option》
Select(sel).select_by_visible_text("每页50条")
sleep(3)

# 根据下拉选项的索引进行选择
Select(sel).select_by_index(0)
sleep(3)

driver.quit()

#
"""
Select 类：用于定位<select>标签。
select_by_value()：通过 value 值定位下拉选项。
select_by_visible_text()：通过 text 值定位下拉选项。
select_by_index()：根据下拉选项的索引进行选择。第一个选项为 0，第二个选项为 1。
"""
