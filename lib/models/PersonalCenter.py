from lib.models import Page
import random, time
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

    def get_random_select_job_course_is_learning_status(self):
        """
        随机选择就业课的学习状态=“开始学习”的就业课
        :return:
        """
        learning_status = self.driver.find_elements_by_link_text("开始学习")
        if len(learning_status) == 0:
            raise exceptions.NoSuchElementException("该账号下没有学习状态为正在学习的就业课")
        learning_study = learning_status[random.randint(0, len(learning_status) - 1)]

        return learning_study

    def get_random_select_job_course_is_expired_status(self):
        """
        随机选择就业课的学习状态=“课程已过期”的就业课
        :return:
        """
        expired_status = self.driver.find_elements_by_link_text("课程已过期")
        if len(expired_status) == 0:
            raise exceptions.NoSuchElementException("该账号下没有学习状态为课程已过期的就业课")
        job_courses_expired = expired_status[random.randint(0, len(expired_status) - 1)]

        return job_courses_expired

    def get_expired_status_tips(self):
        """
        已过期状态的就业课，温馨提示处理
        :return:
        """

        tips_language = self.driver.find_element_by_css_selector("div.recoverTip1 p")
        tips_yes = self.driver.find_element_by_css_selector("div.recoverTip1 a.yes")

        return tips_language, tips_yes

    def get_messages_for_job_course(self, job_course):
        """
        获取就业课的课程信息
        :param job_course:
        :return:
        job_course_url = 课程url
        job_course_name = 岗位课名称
        learning_status = 学习状态【开始学习，已过期】
        finished_percentage = 完成百分比
        notes = 笔记
        questions_and_answer = 问答
        comment = 评论
        course_validity = 课程有效期
        """

        job_course_url = job_course.find_element_by_css_selector("a.courseImg").get_attribute("href")
        job_course_name = job_course.find_element_by_css_selector("a.courseTitle")
        learning_status = job_course.find_element_by_css_selector("a.btn_study")
        finished_percentage = job_course.find_element_by_css_selector("div.courseInfo div.coursePro")
        course_note = job_course.find_elements_by_css_selector("ul.courseNote li")
        notes = course_note[0]
        questions_and_answer = course_note[1]
        comment = course_note[2]
        course_validity = job_course.find_element_by_css_selector("div.courseInfo span")

        return job_course_url, job_course_name, learning_status, finished_percentage, notes, \
                questions_and_answer, comment, course_validity

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

    def get_is_valid_learning_status(self):
        """
        获取有效的课程状态 = 开始学习
        :return:
        """

        learning_status = self.get_messages_for_job_course(self.get_random_select_job_course())[2].text
        while learning_status is True:
            if learning_status == "开始学习":
                break
            else:
                learning_status = self.get_messages_for_job_course(self.get_random_select_job_course())[2].text

    def get_random_select_job_course_note(self):
        """
        随机选择课程笔记
        :return:
        """

        notes = self.driver.find_elements_by_css_selector("ul.all-note li")
        if len(notes) == 0:
            raise exceptions.NoSuchElementException("该就业课下没有笔记")
        note = notes[random.randint(0, len(notes) - 1)]

        return note

    def get_note_content(self, note):
        """
        获取笔记内容
        :return:
        """

        note_content = note.find_element_by_css_selector("div.note-text")

        return note_content

    def act_job_course_note_edit(self, note):
        """
        修改就业课课程笔记
        :return:
        """
        note.find_element_by_css_selector("a.note-edit").click()

        input_box = self.driver.find_element_by_css_selector("textarea.p-note-area")
        input_box.clear()
        input_box.send_keys("修改笔记内容")

        time.sleep(3)
        # self.driver.find_element_by_link_text("提交").click()

        self.driver.find_element_by_css_selector("button.note-save").click()

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
