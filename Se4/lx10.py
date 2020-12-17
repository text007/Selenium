# is_displayed()方法自己实现元素显示等待。

from time import sleep, ctime
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# ctime():当前时间
print(ctime())

for i in range(10):
    """is_displayed() 方法循环判断元素是否可见"""
    try:
        el = driver.find_element_by_id("kw22")
        if el.is_displayed():
            break
    except:
        pass
    # 等待一秒
    sleep(1)
else:
    print("time out")

# ctime():当前时间
print(ctime())

# driver.quit()
