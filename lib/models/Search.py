import random

from lib.models import Page
from lib.models.Teachers import Teachers

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


class Search(Page):
    """
    搜索页模型
    """
    def search(self):
        """
        搜索
        :return:
        """
        search_content = ['java', '测试', '霍荣慧']
        self.driver.find_element_by_css_selector('input.search-key').send_keys(random.choice(search_content))