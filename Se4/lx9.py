# 设置元素等待
# 显式等待

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://baidu.com")

# WebDriverWait(driver, 5, 0.5):每隔 0.5秒检测一次，5秒后下抛出 NoSuchElementException 异常。
# until(EC.visibility_of_element_located((By.ID, "kw"))):调用 expected_conditions 的 visibility_of_element_located方法
# 判断元素(By.ID, "kw")是否存在。
element = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located((By.ID, "kw")))

element.send_keys("selenium")
driver.quit()

# 显式等待是 WebDriver 等待某个条件成立则继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）.

# WebDriverWait()一般与 until()或 until_not()方法配合使用，下面是 until()和 until_not()方法的说明。
"""
until(method, message=″)
调用该方法提供的驱动程序作为一个参数，直到返回值为 True。

until_not(method, message=″)
调用该方法提供的驱动程序作为一个参数，直到返回值为 False。

until_not()方法:
title_is                                    判断当前页面的标题是否等于预期
title_contains                              判断当前页面的标题是否包含预期字符串
presence_of_element_located                 判断元素是否被加在 DOM 树里，并不代表该元素一定可见
visibility_of_element_located               判断元素是否可见（可见代表元素非隐藏，并且元素的宽和高都不等于 0）
visibility_of                               与上一个方法作用相同，上一个方法的参数为定位，该方法接收的参数为定位后的元素
presence_of_all_elements_located            判断是否至少有一个元素存在于 DOM 树中。例如，在页面中有 n 个元素的 class 为“wp”，那么只要有一个元素存在于 DOM 树中就返回 True
text_to_be_present_in_element               判断某个元素中的 text 是否包含预期的字符串
text_to_be_present_in_element_value         判断某个元素的 value 属性是否包含预期的字符串
frame_to_be_available_and_switch_to_it      判断该表单是否可以切换进去，如果可以，返回 True 并且切换进去，否则返回 False
invisibility_of_element_located             判断某个元素是否不在 DOM 树中或不可见
element_to_be_clickable                     判断某个元素是否可见并且是可以点击的
staleness_of                                等到一个元素从 DOM 树中移除
element_to_be_selected                      判断某个元素是否被选中，一般用在下拉列表中
element_selection_state_to_be               判断某个元素的选中状态是否符合预期
element_located_selection_state_to_be       与上一个方法作用相同，只是上一个方法参数为定位后的元素，该方法接收的参数为定位
alert_is_present                            判断页面上是否存在 alert
"""
