from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://baidu.com")

driver.find_element_by_id("kw").send_keys("Seleniun")
driver.find_element_by_id("su").click()
driver.quit()
