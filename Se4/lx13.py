# 多表单切换
# switch_to.frame()方法将当前定位的主体切换为 frame/iframe 表单的内嵌页面。

from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.126.com")
sleep(2)

login_frame = driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
sleep(2)
# 切换表单。
driver.switch_to.frame(login_frame)
sleep(2)
driver.find_element_by_name("email").send_keys("username")
sleep(2)
driver.find_element_by_name("password").send_keys("username")
sleep(2)
driver.find_element_by_id("dologin").click()
sleep(2)
# 回到最外层的页面。
driver.switch_to.default_content()

# driver.quit()
