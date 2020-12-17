# 操作 Cookie

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 获取所有 Cookie 信息并打印
cookie = driver.get_cookies()
# print(cookie)

# 添加 Cookie 信息
driver.add_cookie({"name": "key-aaaaaaa", "value": "value-bbbbbb"})

# 遍历指定的 Cookies
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie["name"], cookie["value"]))

driver.quit()

# Cookie
"""
get_cookies()：获得所有 Cookie。
get_cookie(name)：返回字典中 key 为“name”的 Cookie。 
add_cookie(cookie_dict)：添加 Cookie。 
delete_cookie(name,optionsString)：删除名为 OpenString 的 Cookie。 
delete_all_cookies()：删除所有 Cookie。
"""
