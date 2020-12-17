# 下载文件

import os
from selenium import webdriver

# 修改浏览器下载设置
fp = webdriver.FirefoxProfile()

# 修改下载目录选项。（0：下载到默认路径；2：下载到指定目录）
fp.set_preference("browser.download.folderList", 2)
# 下载到指定目录。（os.getcwd()：当前目录）
fp.set_preference("browser.download.dir", os.getcwd())
# 指定要下载文件的类型。（“binary/octet-stream”用于表示二进制文件）
fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                  "binary/octet-stream")

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_link_text("selenium-3.141.0.tar.gz").click()
