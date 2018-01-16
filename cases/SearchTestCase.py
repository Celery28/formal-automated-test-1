from lib.unittest_ import TestCase
from lib import models
from lib.common import decorators


class SearchTestCase(TestCase):
    """
    搜索测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.search = models.Teachers(cls.driver, cls.config.URL.search_url)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索课程失败")
    def test_search_course(self):
        """搜索课程"""
        pass

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索帖子失败")
    def test_search_post(self):
        """搜素帖子"""
        pass

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索老师失败")
    def test_search_teacher(self):
        """搜索老师"""
        pass

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索学友失败")
    def test_search_student(self):
        """搜素学友"""
        pass
