from lib import models

from selenium.common import exceptions


class PostCourse(models.Page):
    """
    岗位课详情页.
    """

    def get_next_course(self):
        """
        获取下一课的状态.

        :return:
        """
        try:
            next_course = self.driver.find_element_by_css_selector("div.nextCourse span")
            return next_course
        except exceptions.NoSuchElementException:
            return None

    def get_next_course_name(self):
        """
        获取下一课的名称.

        :return:
        """
        try:
            next_course_name = self.driver.find_element_by_css_selector("div.nextCourse p")
            return next_course_name
        except exceptions.NoSuchElementException:
            return None

    def has_next_course(self):
        """
        验证是否有下一课.
        
        :return: 
        """
        next_course = self.get_next_course()

        return False if next_course is None else True

    def act_click_next_course(self):
        """
        点击进入下一课

        :return:
        """

        next_course = self.get_next_course()
        if next_course is None:
            raise exceptions.NoSuchElementException("该岗位课没有下一课")
        else:
            next_course.click()
