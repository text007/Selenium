# 定位一组元素

from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 定位一组元素
texts = driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")

# 计算匹配结果数
print(len(texts))

# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()

# 8 种用于定位一组元素的方法。
"""
定位一组元素的方法与定位单个元素的方法非常像，唯一的区别是单词“element”后面多了一个“s”，用来表示复数。
find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()
"""
