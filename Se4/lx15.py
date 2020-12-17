# 警告框处理

from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# 打开搜索设置
link = driver.find_element_by_id("s-usersetting-top").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(3)

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
sleep(3)


# 获取警告框
alert = driver.switch_to.alert
sleep(3)

# 获取警告框提示信息
alert_text = alert.text
sleep(3)
print(alert_text)

# 接受警告框
alert.accept()

driver.quit()

"""
text：返回 alert、confirm、prompt 中的文字信息。
accept()：接受现有警告框。
dismiss()：解散现有警告框。
send_keys()：在警告框中输入文本（如果可以输入的话）。
"""
