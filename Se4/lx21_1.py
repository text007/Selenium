from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://videojs.com/')
video=driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')
url=driver.execute_script('return arguments[0].currentSrc;',video)
print(url)

print('start')
driver.execute_script('arguments[0].play()',video)

sleep(15)

print('stop')
driver.execute_script('arguments[0].pause()',video)
# driver.quit()