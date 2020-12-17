# 模块化与参数化

from time import sleep
from selenium import webdriver
from module import Mail
from read_txt import users

driver = webdriver.Firefox()
driver.get("http://www.126.com")


# 调用 Mail 类并接收 driver 驱动
mail = Mail(driver)

# 登录
mail.login(users[0][0], users[0][1])

mail.login(users[1][0], users[1][1])

mail.login(users[2][0], users[2][1])

mail.login(users[3][0], users[3][1])

mail.login(users[4][0], users[4][1])

# 登录之后的操作
sleep(5)

# 退出
mail.logout()

driver.quit()
