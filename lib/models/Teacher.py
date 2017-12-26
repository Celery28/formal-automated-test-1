import random

from lib.models import Page

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


class Teacher(Page):
    """
    教师详情页模型
    """

    def is_vote_for_teacher(self) -> bool:
        """
        判断是否已经对教师点赞.

        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a.teacher-zan-on')
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_favorite_for_teacher(self) -> bool:
        """
        判断是否已经关注教师.

        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a.teach-has-sc')
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_un_favorite_for_teacher(self) -> bool:
        """
        检查是否未关注教师.

        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a.teach-no-sc')
            return True
        except exceptions.NoSuchElementException:
            return False

    def act_click_favorite(self) -> None:
        """
        点击关注按钮.

        :return void:
        """
        try:
            self.driver.find_element_by_css_selector('a.teach-no-sc').click()
        except exceptions.NoSuchElementException:
            pass

    def act_click_cancel_favorite(self) -> None:
        """
        点击取消关注按钮.

        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a.teach-has-sc').click()
        except exceptions.NoSuchElementException:
            pass