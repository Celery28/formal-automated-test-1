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

    @decorators.TestCaseDecorators.screen_shot_in_except("进入金牌讲师界面失败")
    def test_act_teachers(self):
        """验证进入金牌讲师界面"""
        self.homepage.act_teachers()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, "http://www.kgc.cn/teachers", "测试不通过")
