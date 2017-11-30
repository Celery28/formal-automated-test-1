from lib.unittest_ import TestCase
from lib import models
from lib.common import decorators


class TeachersTestCase(TestCase):
    """
    教师列表页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.teachers = models.Teachers(cls.driver)

    def setUp(self):
        """
        将关闭浏览器标签的标志设置为False.

        :return:
        """
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("随机选择教师方向失败")
    def test_teachers_category(self):
        """
        随机筛选教师方向

        :return:
        """
        self.teachers.act_click_teachers_category()
        category_name = self.teachers.get_current_teachers_category()
        print(self.driver.title)

        self.assertIn(category_name, self.driver.current_url, "测试不通过")

