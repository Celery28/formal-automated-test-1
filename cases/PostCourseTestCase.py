from lib import models
from lib.unittest_ import TestCase
from lib.common import decorators


class PostCourseTestCase(TestCase):
    """
    岗位详情页测试用例.
    
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.post_courses = models.PostCourses(cls.driver)

    @decorators.TestCaseDecorators.screen_shot_in_except("点击进入下一课失败")
    def test_next_course(self):
        """
        测试进入下一课
    
        :return:
        """

        course = self.post_courses.act_click_random_post_course()

        if course.has_next_course() is False:
            pass

        course.act_click_next_course()
        self.assertIn('', '', '')