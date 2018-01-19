from lib.unittest_ import TestCase
from lib import models
from lib.common import decorators


class SeriesCourseTestCase(TestCase):
    """
    系列集合页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.search = models.SeriesCourse(cls.driver, cls.config.URL.series_course_url)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""

        self.close_browser_current_tab_on_tear_down = False