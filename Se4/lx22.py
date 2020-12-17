# 滑动解锁

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Firefox()
driver.get("https://www.helloweba.com/demo/2017/unlock/")

# 定位滑块元素
slider = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
# 鼠标悬停
action = ActionChains(driver)
# 单击并按下鼠标左键
action.click_and_hold(slider).perform()

# 向右循环移动直至解锁位置
for index in range(200):
    try:
        action.move_by_offset(2, 0).perform()
    except UnexpectedAlertPresentException:
        break
    action.reset_actions()
    sleep(0.1)

# 打印警告提示
success_text = driver.switch_to.alert.text
print(success_text)
