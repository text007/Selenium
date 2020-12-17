# 定位元素(百度首页)
# id 定位
"""
id 在 HTML 文档中必须是唯一的
find_element_by_id("kw")
find_element_by_id("su")
"""

# name 定位
"""
name 用来指定元素的名称
find_element_by_name("wd")
"""

# class 定位
"""
class 用来指定元素的类名
find_element_by_class_name("s_ipt")
"""

# tag 定位
"""
tag 来定义不同页面的元素
find_element_by_tag_name("input")
"""

# link 定位
"""
link 定位文本链接
find_element_by_link_text("新闻")
find_element_by_link_text("hao123")
find_element_by_link_text("地图")
find_element_by_link_text("视频")
find_element_by_link_text("贴吧")
"""

# partial link 定位
"""
partial link 取文字链接的部分文字进行定位
    <a class="mnav" name="tj_lang" href="#">一个很长的文本链接</a>
find_element_by_partial_link_text("一个很长的")
find_element_by_partial_link_text("文本链接")
"""


# XPath 定位
# 绝对路径定位
"""
根据代码层级结构写出元素的绝对路径
find_element_by_xpath("/html/body/div/div[2]/div/div/div/from/span/input")
find_element_by_xpath("/html/body/div/div[2]/div/div/div/from/span[2]/input")

主要用标签名的层级关系来定位元素的绝对路径，最外层为 html，在 body 文本内，一级一级往下查找。
如果一个层级下有多个相同的标签名，那么就按上下顺序确定是第几个。
例如，div[2]表示当前层级下第二个 div 标签。
"""

# 利用元素属性定位
"""
find_element_by_xpath("//input[@id='kw']")
find_element_by_xpath("//input[@id='su']")
//input 表示当前页面某个 input 标签，[@id='kw'] 表示这个元素的 id 值是 kw。

通过 name 和 class 来定位。
find_element_by_xpath("//*[@name='wd']")
find_element_by_xpath("//*[@class='s_ipt']")
不想指定标签名，那么可以用星号（*）代替.

find_element_by_xpath("//input[@maxlength='100']")
find_element_by_xpath("//input[@autocomplete='off']")
find_element_by_xpath("//input[@type='submit']")
"""

# 层级与属性结合
"""
find_element_by_xpath("//span[@class='bg s_ipt_wr']/input")
span[@class='s_ipt_wr'] 通过 class 定位到父元素，后面的/input 表示父元素下面的子元
素。

find_element_by_xpath("//form[@id='form']/span/input")
find_element_by_xpath("//form[@id='form']/span[2]/input")
"""

# 使用逻辑运算符
"""
使用逻辑运算符连接多个属性来查找元素。
find_element_by_xpath("//input[@id='kw' and @class='s_ipt']")
"""

# 使用 contains 方法
"""
contains 方法用于匹配一个属性中包含的字符串。
find_element_by_xpath("//span[contains(@calss,'s_ipt_wr')]/input")
contains 方法只取了 class 属性中的“s_ipt_wr”部分。
"""

# 使用 text()方法
"""
text()方法用于匹配显示文本信息。
find_element_by_xpath("//a[text(),'新闻')]")

contains 和 text()也可以配合使用。
find_element_by_xpath("//a[contains(text(),'一个很长的')]")
"""


# CSS 定位
"""
选择器             例子               描 述
.class            .intro            class 选择器，选择 class="intro"的所有元素
#id               #firstname        id 选择器，选择 id="firstname"的所有元素
*                 *                 选择所有元素
element           p                 选择所有<p>元素
element > element div > input       选择父元素为 <div>的所有 <input> 元素
element + element div + input       选择同一级中紧接在 <div> 元素之后的所有 <input> 元素
[attribute=value] [target=_blank]   选择 target="_blank" 的所有元素
"""

# 通过 class 定位
"""
find_element_by_css_selector(".s_ipt")
find_element_by_css_selector(".s_btn")
ind_element_by_css_selector()方法用于在 CSS 中定位元素，点号（.）表示通过 class 来定位元素。
"""

# 通过 id 定位
"""
find_element_by_css_selector("#kw")
find_element_by_css_selector("#su")
井号（#）表示通过 id 来定位元素。
"""

# 通过标签名定位
"""
find_element_by_css_selector("input")
用标签名定位元素时不需要任何符号标识，直接使用标签名即可。
"""

# 通过标签层级关系定位
"""
find_element_by_css_selector("span > input")
这种写法表示有父元素，父元素的标签名为 span。查找 span 中所有标签名为 input 的子元素。
"""

# 通过属性定位
"""
find_element_by_css_selector("[autocomplete=off]")
find_element_by_css_selector("[name='kw']")
find_element_by_css_selector('[type="submit"]')
可以加引号，也可以不加，注意和整个字符串的引号进行区分。
"""

# 组合定位
"""
find_element_by_css_selector("form.fm > span > input.s_ipt")
find_element_by_css_selector("form#form > span > input#kw")
要定位的这个元素标签名为 input，这个元素的 class 属性为 s_ipt；并且它有一个父元素，标签名为 span。
它的父元素还有父元素，标签名为 form，class 属性为 fm。
"""

# 更多定位用法
"""
find_element_by_css_selector("[class*=s_ipt_wr]")
查找 class 属性包含“s_ipt_wr”字符串的元素。

find_element_by_css_selector("[class^=bg]")
查找 class 属性以“bg”字符串开头的元素。

find_element_by_css_selector("[class$=wrap]")
查找 class 属性以“wrap”字符串结尾的元素。

find_element_by_css_selector("form > input:nth-child(2)")
查找 form 标签下面第 2 个 input 标签的元素。
"""


# 用 By 定位元素
"""
find_element(By.ID,"kw")
find_element(By.NAME,"wd")
find_element(By.CLASS_NAME,"s_ipt")
find_element(By.TAG_NAME,"input")
find_element(By.LINK_TEXT,"新闻")
find_element(By.PARTIAL_LINK_TEXT,"新")
find_element(By.XPATH,"//*[@class='bg s_btn']")
find_element(By.CSS_SELECTOR,"span.bg s_btn_wr>input#su")
find_element()方法只用于定位元素，它需要两个参数。
第一个参数是定位的类型，由 By 提供；第二个参数是定位的值，在使用 By 之前需要先导入。

return self.find_element(by=By.ID, value=id_)
"""


# 控制浏览器
# 控制浏览器窗口大小
"""
WebDriver 提供的 set_window_size()方法可以用来设置浏览器窗口大小。
driver.set_window_size(480, 800)
"""

# 控制浏览器后退、前进
"""
WebDriver 还提供了对应的 back()和 forward()方法来模拟后退和前进按钮。
后退: driver.back()
前进: driver.forward()
"""

# 模拟浏览器刷新
"""
refresh()方法实现浏览器刷新
driver.refresh() #刷新当前页面
"""


# WebDriver 中的常用方法
# （1）clear()：清除文本。
"""
driver.find_element_by_id("kw").clear()
"""

# （2）send_keys(value)：模拟按键输入。
"""
driver.find_element_by_id("kw").send_keys("selenium")
"""

# （3）click()：单击元素。
"""
driver.find_element_by_id("su").click()
"""

# （4）submit()：提交表单。
"""
通过按键盘上的回车键完成搜索内容的提交
search.submit()
"""

# （5）size：返回元素的尺寸。
"""
size = driver.find_element_by_id('kw').size
"""

# （6）text：获取元素的文本。
"""
text = driver.find_element_by_id("cp").text
"""

# （7）get_attribute(name)：获得属性值。
"""
返回元素的属性值，可以是 id、name、type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
"""

# （8）is_displayed()：设置该元素是否用户可见。
"""
返回元素的结果是否可见，返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
"""


# 鼠标操作
"""
 perform()：执行 ActionChains 类中存储的所有行为。
context_click()：右击。 
double_click()：双击。 
drag_and_drop()：拖动。 
move_to_element()：鼠标悬停。
"""

# 鼠标悬停操作
"""
对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
"""


# 键盘操作
"""
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

# Ctrl+a、Ctrl+c、Ctrl+c 组合键
"""
输入组合键 Ctrl+a，全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

输入组合键 Ctrl+x，剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

输入组合键 Ctrl+v，粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
"""


# 获取验证消息
"""
title：用于获取当前页面的标题。
current_url：用于获取当前页面的 URL。 
text：用于获取当前页面的文本信息。
"""


# 设置元素等待
# 显式等待
"""
显式等待是 WebDriver 等待某个条件成立则继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）。

WebDriverWait 类是 WebDriver 提供的等待方法。
在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间仍检测不到，则抛出异常。

WebDriverWait()一般与 until()或 until_not()方法配合使用，下面是 until()和 until_not()方法的说明。
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

# 隐式等待
"""
WebDriver 提供的 implicitly_wait()方法可用来实现隐式等待，用法相对来说要简单得多。
driver.implicitly_wait(10)
"""


# 定位一组元素
"""
定位一组元素的方法与定位单个元素的方法非常像，唯一的区别是单词“element”后面多了一个“s”，用来表示复数。

find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()
"""


# 多表单切换
"""
通过 switch_to.frame()方法将当前定位的主体切换为 frame/iframe 表单的内嵌页面。
通过 switch_to.default_content()回到最外层的页面。
"""


# 多窗口切换
"""
WebDriver 提供的 switch_to.window()方法可以实现在不同的窗口间切换。
current_window_handle：获得当前窗口句柄。
window_handles：返回所有窗口的句柄到当前会话。
switch_to.window()：切换到相应的窗口。
"""


# 警告框处理
"""
text：返回 alert、confirm、prompt 中的文字信息。
accept()：接受现有警告框。
dismiss()：解散现有警告框。
send_keys()：在警告框中输入文本（如果可以输入的话）。

driver.switch_to.alert
"""


# 下拉框处理
"""
Select 类：用于定位<select>标签。
select_by_value()：通过 value 值定位下拉选项。
select_by_visible_text()：通过 text 值定位下拉选项。
select_by_index()：根据下拉选项的索引进行选择。第一个选项为 0，第二个选项为 1。
"""


# 上传文件
"""
通过 send_keys() 指定本地文件路径的方式实现文件上传。
driver.find_element_by_id("inputfile").send_keys(file_path + "\\test.txt")

lx14.py
"""


# 下载文件
"""
修改 Firefox 浏览器下载（FirefoxProfile()）设置：
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "binary/octet-stream")
driver = webdriver.Firefox(firefox_profile=fp)

browser.download.folderList：设置为 0，表示文件会下载到浏览器默认的下载路径；设置为 2，表示文件会下载到指定目录。
browser.download.dir：用于指定下载文件的目录。通过 os.getcwd()方法获取当前文件的所在位置，即下载文件保存的目录。
browser.helperApps.neverAsk.saveToDisk：指定要下载文件的类型，即 Content-type 值，“binary/octet-stream”用于表示二进制文件。

修改 Chrome 浏览器下载（ChromeOptions()）设置：
options = webdriver.ChromeOptions() 
prefs = {'profile.default_content_settings.popups': 0,'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs) 
driver = webdriver.Chrome(chrome_options=options)

profile.default_content_settings.popups：设置为 0，表示禁止弹出下载窗口。
download.default_directory：设置文件下载路径，使用 os.getcwd()方法获取当前脚本的目录作为下载文件的保存位置。
"""


# 操作 Cookie
"""
要验证浏览器中的 Cookie 是否正确
get_cookies()：获得所有 Cookie。 
get_cookie(name)：返回字典中 key 为“name”的 Cookie。 
add_cookie(cookie_dict)：添加 Cookie。 
delete_cookie(name,optionsString)：删除名为 OpenString 的 Cookie。 
delete_all_cookies()：删除所有 Cookie。

# 获得所有 Cookie 信息
cookie = driver.get_cookies()
# 添加 Cookie 信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})
"""


# 调用 JavaScript
# 浏览器滚动条的拖动
"""
window.scrollTo()方法用于设置浏览器窗口滚动条的水平位置和垂直位置。第一个参数表示水平的左边距，第二个参数表示垂直的上边距
js = "window.scrollTo(100,450);"
"""

# 在页面中的 textarea 文本框中输入内容
"""
将 text 与 JavaScript 代码通过“+”进行拼接，这样做的目的是为了方便自定义输入内容。最后，通过 execute_script()执行 JavaScript 代码。
text = "input text"
js = "document.getElementById('id').value='" + text + "';"
driver.execute_script(js)
"""


# 处理 HTML5 视频播放
"""
JavaScript 有个内置的对象叫作 arguments。arguments 包含了函数调用的参数数组，[0]表示取对象的第 1 个值。
currentSrc 返回当前音频/视频的 URL。如果未设置音频/视频，则返回空字符串。
load()、play()和 pause() 控制视频的加载、播放和暂停。

driver.execute_script("return arguments[0].currentSrc;", video)
"""


# 滑动解锁
"""
click_and_hold()： 单击并按下鼠标左键，在鼠标事件中介绍过。
 move_by_offset()：移动鼠标，第一个参数为 x 坐标距离，第二个参数为 y 坐标距离。
 reset_action()：重置 action。
"""

# 上下滑动选择日期
"""
lement：滑动的元素。
 xoffset：x 坐标距离。
 yoffset：y 坐标距离。

webdriver.TouchActions(driver).scroll_from_element(year, 0, 5).perform()
"""


# 窗口截图
"""
WebDriver 提供了截图函数 save_screenshot ()，可用来截取当前窗口。

# 截取当前窗口，指定截图图片的保存位置
driver.save_screenshot("./files/baidu_img.png")
"""

# 关闭窗口
"""
quit()方法，其含义为退出相关的驱动程序和关闭所有窗口。
WebDriver 还提供了 close()方法，用来关闭当前窗口。
"""
