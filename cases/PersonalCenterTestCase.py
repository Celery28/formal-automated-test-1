from lib.unittest_ import TestCase
from lib import models
from lib.common import decorators


class PersonalCenterTestCase(TestCase):
    """
    个人中心页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.personal_center = models.PersonalCenter(cls.driver, cls.config.URL.personal_center)
        cls.login = models.Login(cls.driver)
        cls.login.act_login(cls.config.User.username, cls.config.User.password)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""
        self.close_browser_current_tab_on_tear_down = False
