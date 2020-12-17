
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.126.com")
sleep(2)

driver.find_element_by_name("email").send_keys("username")
sleep(2)
driver.find_element_by_name("password").send_keys("username")
sleep(2)
driver.find_element_by_id("dologin").click()

# driver.quit()
