from lib.models import Page
import random
from selenium.common import exceptions


class PersonalCenter(Page):
    """
    个人中心
    """

    def is_exist_employment_courses(self):
        """
        判断是否存在就业课
        :return:
        """
        try:
            self.driver.find_element_by_css_selector("li.qd-job")
            return True
        except exceptions.NoSuchElementException:
            return False

    """
    就业课页面元素动作
    """

    def act_click_job(self):
        """
        点击进入就业课tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-job").click()

    def get_random_select_job_course(self):
        """
        随机选择一节就业课
        :return:
        """
        job_courses = self.driver.find_elements_by_css_selector("ul.list-ul li")
        if len(job_courses) == 0:
            raise exceptions.NoSuchElementException("就业课列表没有找到任何就业课，请检查是否存在问题")
        job_course = job_courses[random.randint(0, len(job_courses) - 1)]

        return job_course

    def get_messages_for_job_course(self, job_course):
        """
        获取就业课的课程信息
        :param job_course:
        :return:
        """

        job_course_url = job_course.find_element_by_css_selector("a.courseImg").get_attribute("href")
        job_course_name = job_course.find_element_by_css_selector("a.courseTitle")
        learning_status = job_course.find_element_by_css_selector("a.btn_study")
        finished_status = job_course.find_element_by_css_selector("div.courseInfo div.coursePro")

        return job_course_url, job_course_name, learning_status, finished_status

    def get_job_course_tab_page(self):
        """
        点击进入就业课的tab页面
        就业课程
        学习计划
        我的自测
        :return:
        """
        job_course_tab_page = self.driver.find_element_by_css_selector("span.cen-note-t a")
        employment_courses = job_course_tab_page[0]
        study_play = job_course_tab_page[1]
        my_test = job_course_tab_page[2]

        return employment_courses, study_play, my_test

    """
    我的课程页面元素动作
    """

    def act_click_course(self):
        """
        点击进入课程tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-course").click()

    """
    个人动态页面元素动作
    """

    def act_click_news(self):
        """
        点击进入动态tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-news").click()

    """
    个人中心——题库页面元素动作
    """

    def act_click_question(self):
        """
        点击进入题库tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-square").click()

    """
    社区页面元素动作
    """

    def act_click_community(self):
        """
        点击进入社区tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-usercare").click()

    """
    任务页面元素动作
    """

    def act_click_task(self):
        """
        点击进入任务tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-task").click()

    """
    钱包页面元素动作
    """

    def act_click_wallet(self):
        """
        点击进入钱包tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-qnd").click()

    """
    设置页面元素动作
    """

    def act_click_set(self):
        """
        点击进入设置tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-set").click()
