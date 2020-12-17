
from base import BasePage


class BaiduPage(BasePage):

    url = "https://www.baidu.com"

    def search_input(self, search_key):
        self.driver.find_element_by_id("kw").send_keys(search_key)

    def search_button(self):
        self.by_id("su").click()
