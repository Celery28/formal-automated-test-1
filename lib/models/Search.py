import random

from lib.models import Page
from lib.models.Teachers import Teachers

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


class Search(Page):
    """
    搜索页模型
    """

    search_content = ['java', '测试']

    def act_click_search(self):
        """
        随机搜素某些关键字
        :return:
        """
        self.driver.find_element_by_css_selector('input.search-key').send_keys(random.choice(self.search_content))
        self.driver.find_element_by_css_selector('a.search1-btn').click()

    def act_switch_to_course(self):
        """

        :return:
        """
