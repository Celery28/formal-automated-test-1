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

    def is_exist_same_teacher_direction(self):
        """
        检查是否存在同方向其他讲师
        :return:
        """
        try:
            self.driver.find_element_by_link_text("同方向其他讲师")
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_exist_gold_medal_teacher(self):
        """
        检查是否存在金牌讲师
        :return:
        """

        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]")
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_exist_course_video(self):
        """
        检查是否存在课程视频
        :return:
        """

        try:
            self.driver.find_element_by_link_text("课程视频")
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_exist_course_pages(self):
        """
        检查是否存在课程分页
        :return:
        """

        try:
            self.driver.find_element_by_css_selector("div.pager")
            return True
        except exceptions.NoSuchElementException:
            return False

    def get_random_course_video(self):
        """
        随机选择课程
        :return:
        """

        courses = self.driver.find_elements_by_css_selector("ul.box-img li")
        if len(courses) == 0:
            raise exceptions.NoSuchElementException("没有找到任何课程")
        course = courses[random.randint(0, len(courses) - 1)]

        return course

    def get_random_course_pages(self):
        """
        随机选择课程分页
        :return:
        """
        pages = self.driver.find_elements_by_css_selector("ul.yiiPager li")
        if len(pages) == 0:
            raise exceptions.NoSuchElementException("没有找到任何任何分页")
        page = pages[random.randint(2, len(pages) - 1)]

        return page

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

    def act_click_vote_for_teacher(self) -> None:
        """
        对教师点赞.

        :return:
        """
        self.driver.find_element_by_css_selector("span.teacher-zan-num").click()

    def act_click_random_same_teacher_direction(self):
        """
        随机点击同方向的教师
        :return:
        """
        pass

    def act_click_random_gold_medal_teacher(self):
        """
        随机点击金牌讲师
        :return:
        """
        pass
