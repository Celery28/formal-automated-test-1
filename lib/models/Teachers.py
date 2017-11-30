import random

from lib.models import Page

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


class Teachers(Page):
    """
    教师列表页模型
    """

    url = 'http://www.kgc.cn/teachers'

    def get_random_teachers_category(self):
        """
        随机获取教师方向并点击

        :return:
        """
        teachers_category = self.driver.find_elements_by_css_selector("div.yui3-u-7-8 li")
        if len(teachers_category) == 0:
            raise exceptions.NoSuchElementException("没有找到课程方向")

        teacher_category = teachers_category[random.randint(1, len(teachers_category) - 1)]
        click_category_name = teacher_category.text
        teacher_category.click()

        return click_category_name

    def get_current_teachers_category(self):
        """
        获取当前选中的教师方向名称

        :return:
        """
        category_name = self.driver.find_elements_by_css_selector("div.yui3-u-7-8 li a[class='on']")
        if not category_name:
            raise exceptions.NoSuchElementException("没有找到选中的教师方向")

        return category_name[0]


