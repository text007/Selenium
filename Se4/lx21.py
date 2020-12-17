# 处理 HTML5 视频播放

from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://videojs.com/")

video = driver.find_element_by_id('preview-player_html5_api')

# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

print("start")
driver.execute_script('arguments[0].play()', video)

# 播放 15s
sleep(15)

# 暂停视频
print("stop")
driver.execute_script("arguments[0].pause()", video)

# driver.quit()
