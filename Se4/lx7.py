# 键盘操作

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 在输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")

# 删除多输入的一个m
time.sleep(2) # 暂停2秒
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+ “教程”
time.sleep(2) # 暂停2秒
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(2) # 暂停2秒
driver.find_element_by_id("kw").send_keys("教程")

# 输入组合键 Ctrl+a, 全选输入框内容
time.sleep(2) # 暂停2秒
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")

# 输入组合键Ctrl+x，剪切输入框内容
time.sleep(2) # 暂停2秒
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")

# 输入框组合键Ctrl+v，粘贴输入框内容
time.sleep(2) # 暂停2秒
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "v")

# 用回车键代替点击操作
time.sleep(2) # 暂停2秒
driver.find_element_by_id("su").send_keys(Keys.ENTER)

driver.quit()

"""
以下为常用的键盘操作。
send_keys(Keys.BACK_SPACE)：删除键（BackSpace）
send_keys(Keys.SPACE)：空格键（Space） 
send_keys(Keys.TAB)：制表键（Tab） 
send_keys(Keys.ESCAPE)：回退键（Esc） 
send_keys(Keys.ENTER)：回车键（Enter） 
send_keys(Keys.CONTROL,'a')：全选（Ctrl+a） 
send_keys(Keys.CONTROL,'c')：复制（Ctrl+c） 
send_keys(Keys.CONTROL,'x')：剪切（Ctrl+x） 
send_keys(Keys.CONTROL,'v')：粘贴（Ctrl+v） 
send_keys(Keys.F1)：键盘 F1
……
send_keys(Keys.F12)：键盘 F12
"""
