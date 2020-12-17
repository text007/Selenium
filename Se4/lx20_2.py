# 调用 JavaScript
# 在页面中的 textarea 文本框中输入内容

import os
from selenium import webdriver

texts = os.path.abspath("./files//")

driver = webdriver.Firefox()
upload_page = "file:///" + texts + "/lx20_1.html"
driver.get(upload_page)

text = "input text"
js = "document.getElementById('id').value='" + text + "';"
driver.execute_script(js)
