from lib.unittest_ import TestCase
from lib import models
from lib.common import decorators
import time


class PersonalCenterTestCase(TestCase):
    """
    个人中心页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.personal_center = models.PersonalCenter(cls.driver, cls.config.URL.homepage_url)
        cls.login = models.Login(cls.driver)
        cls.login.act_login(cls.config.User.username, cls.config.User.password)
        cls.driver.find_element_by_id("header-login-nickname-str").click()

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课随机点击开始学习失败")
    def test_job_course_learning_status(self):
        """测试就业课随机点击开始学习，进入播放课程列表"""

        self.driver.refresh()

        learning_study = self.personal_center.get_random_select_job_course_is_learning_status()
        course_name = learning_study.get_attribute("data-name")
        learning_study.click()

        course_title = self.driver.find_element_by_css_selector("div.course-title h1.normal")

        self.assertEqual(course_name, course_title.text,
                         "就业课点击开始学习失败，就业课列表显示的课程名称和实际课程名称不一致")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课点击课程已过期状态失败")
    def test_job_courses_expired(self):
        """测试就业课随机点击已过期的状态是否正确"""

        self.driver.refresh()

        job_courses_expired = self.personal_center.get_random_select_job_course_is_expired_status()
        job_courses_expired.click()

        tips_language = self.personal_center.get_expired_status_tips()[0]

        self.assertEqual("该课程已过期，续费请联系中心老师。", tips_language.text,
                         "点击已经过期的就业课状态，提示语有误")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课列表，点击课程名称进入就业课详情页失败")
    def test_job_course_details_page(self):
        """测试就业课列表，点击课程名称进入就业课详情页"""

        self.driver.refresh()

        job_course_name = self.personal_center.get_messages_for_job_course(
            self.personal_center.get_random_select_job_course())[1]
        a = job_course_name.text

        job_course_name.click()

        self.personal_center.act_switch_to_last_window()

        self.assertEqual("{0} - 岗位课 - 课工场".format(a), self.driver.title,
                         "就业课列表，点击课程名称进入就业课详情页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课-修改笔记失败")
    def test_job_course_modify_notes(self):
        """测试就业课-修改笔记功能"""

        self.driver.refresh()

        course = self.personal_center.get_random_select_job_course()
        time.sleep(1)
        self.personal_center.get_messages_for_job_course(course)[4].click()
        time.sleep(1)
        note = self.personal_center.get_random_select_job_course_note()
        time.sleep(1)
        self.personal_center.act_job_course_note_edit(note)
        time.sleep(1)
        note_content = self.personal_center.get_note_content(note)
        time.sleep(1)

        self.assertEqual("修改笔记内容", note_content.text, "就业课修改笔记失败")

