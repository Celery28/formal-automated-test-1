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
    course = "/html/body/div[2]/div/h2/div/span[1]"
    post = "/html/body/div[2]/div/h2/div/span[2]"
    teacher = "/html/body/div[2]/div/h2/div/span[3]"
    user = "/html/body/div[2]/div/h2/div/span[4]"

    def get_search_content(self):
        """
        输入搜索内容，进行搜索
        :return:
        """
        search_key = self.driver.find_element_by_css_selector("input.search-key")
        search_key.clear()
        search_key.send_keys(random.choice(self.search_content))
        self.driver.find_element_by_css_selector("a.search1-btn").click()

    def is_null_search(self):
        """
        判断搜索课程是否为空
        如果为空，返回false
        如果不为空，返回true
        :return:
        """
        try:
            self.driver.find_element_by_css_selector("div.search-empty")
            return False
        except exceptions.NoSuchElementException:
            return True

    def get_random_flip_pages(self):
        """
        随机翻页
        :return:
        """
        pages = self.driver.find_elements_by_css_selector("ul.yiiPager li")
        if len(pages) == 0:
            raise exceptions.NoSuchElementException("没有分页")

        page = pages[random.randint(1, len(pages) - 1)]

        return page

    def get_random_course_for_courses(self):
        """
        从课程列表随机选择课程
        :return:
        """

        courses = self.driver.find_elements_by_css_selector("ul.search-course li")
        if len(courses) == 0:
            raise exceptions.NoSuchElementException("当前搜索结果下没有课程")

        course = courses[random.randint(0, len(courses) - 1)]

        return course

    def get_random_course_label_for_courses(self):
        """
        从课程列表中随机选择课程标签
        :return:
        """
        course = self.get_random_course_for_courses()
        courses_label = course.find_elements_by_css_selector("div.search-c-tag a")
        if courses_label == 0:
            raise exceptions.NoSuchElementException("该课程下没有课程标签")

        course_label = courses_label[random.randint(0, len(courses_label) - 1)]

        return course_label

    def get_random_post_for_posts(self):
        """
        从帖子列表随机选择帖子
        :return:
        """
        posts_list = self.driver.find_elements_by_css_selector("ul.open-sec2-list")
        if len(posts_list) == 0:
            raise exceptions.NoSuchElementException("当前搜索结果下没有相关帖子")
        post = posts_list[random.randint(0, len(posts_list) - 1)]

        return post

    def get_post_plate(self):
        """
        进入帖子板块
        :return:
        """
        pass

    def get_homepage(self):
        """
        进入个人主页
        :return:
        """
        pass

    def get_random_teacher_for_teachers(self):
        """
        从教师列表页随机选择教师
        :return:
        """
        teachers = self.driver.find_elements_by_css_selector("ul.teacher-list li")
        if len(teachers) == 0:
            raise exceptions.NoSuchElementException("当前搜索结果下没有教师")

        teacher = teachers[random.randint(0, len(teachers) - 1)]

        return teacher

    def get_random_course_for_teacher(self):
        """
        从所选教师中随机获取课程
        :return:
        """
        teacher = self.get_random_teacher_for_teachers()
        teacher_courses = teacher.find_elements_by_css_selector("dt.teacher-course-item a")

        return teacher_courses

    def get_name_and_img_for_teacher(self):
        """
        从所选教师中获取教师名称和教师头像
        :return:
        """
        teacher = self.get_random_teacher_for_teachers()

        teacher_name = teacher.find_element_by_css_selector("span.f18")
        teacher_img = teacher.find_element_by_css_selector("div.teacher-tx a img")

        return teacher_name, teacher_img

    def get_random_student_for_students(self):
        """
        从学友列表页随机选择学友
        :return:
        """

        students = self.driver.find_elements_by_css_selector("ul.center-fan-list li")
        if len(students) == 0:
            raise exceptions.NoSuchElementException("当前搜索结果下没有学友")

        student = students[random.randint(0, len(students) - 1)]

        return student

    def act_click_random_attention_for_student(self):
        """
        学友列表页，随机关注某学友
        :return:
        """

        student = self.get_random_student_for_students()
        attention = student.find_element_by_css_selector("a.uc-fan-gz")

        attention.click()

    def act_click_search(self):
        """
        随机搜素某些关键字
        :return:
        """
        self.driver.find_element_by_css_selector('input.search-key').send_keys(random.choice(self.search_content))
        self.driver.find_element_by_css_selector('a.search1-btn').click()

    def act_switch_to_course(self):
        """
        切换到搜索课程界面
        :return:
        """
        courses = self.driver.find_element_by_css_selector("div.search-tab span")[0]

        return courses

    def act_switch_to_post(self):
        """
        切换到搜索帖子界面
        :return:
        """
        posts = self.driver.find_element_by_css_selector("div.search-tab span")[1]

        return posts

    def act_switch_to_teacher(self):
        """
        切换到搜索老师界面
        :return:
        """
        teachers = self.driver.find_element_by_css_selector("div.search-tab span")[2]

        return teachers

    def act_switch_to_student(self):
        """
        切换到搜索学友界面
        :return:
        """
        students = self.driver.find_element_by_css_selector("div.search-tab span")[3]

        return students

