from lib.unittest_ import TestCase
from lib import models
from lib.common import decorators

class HomepageTestcase(TestCase):
    """
    课工场首页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = "Chrome"
        TestCase.setUpClass()
        cls.homepage = models.Homepage(cls.driver)

    def tearDown(self):
        """
        将关闭浏览器标签的标志设置为False
        :return:
        """
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("进入课程库失败")
    def test_act_courses(self):
        """ 验证进入课程库界面"""
        self.homepage.act_courses()
        self.homepage.act_switch_to_last_window()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, "http://www.kgc.cn/list/230-1-6-9-9-0.shtml", "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("进入就业实训界面失败")
    def test_act_employment_base(self):
        """验证进入就业实训基地界面"""
        self.homepage.act_employment_base()
        self.homepage.act_switch_to_last_window()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, "http://a.kgc.cn/", "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("进入岗位课界面失败")
    def test_act_job(self):
        """验证进入岗位课界面"""
        self.homepage.act_job()
        self.homepage.act_switch_to_last_window()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, "http://www.kgc.cn/job", "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("进入金牌讲师界面失败")
    def test_act_teachers(self):
        """验证进入金牌讲师界面"""
        self.homepage.act_teachers()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, "http://www.kgc.cn/teachers", "测试不通过")
