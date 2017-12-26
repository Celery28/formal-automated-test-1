from lib.unittest_ import TestCase
from lib import models
from lib.common import decorators


class TeacherTestCase(TestCase):
    """
    教师详情页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.teachers = models.Teachers(cls.driver)
        cls.login = models.Login(cls.driver)
        cls.login.act_login(cls.config.User.username, cls.config.User.password)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_教师关注验证失败")
    def test_teacher_details_favorite(self):
        """
        测试教师关注/取消关注
        :return: 
        """
        self.teachers.act_click_random_teacher()

        teacher = models.Teacher(self.driver)
        if teacher.is_favorite_for_teacher() is True:
            teacher.act_click_cancel_favorite()
            self.assertTrue(teacher.is_un_favorite_for_teacher(), '点击取消关注教师按钮失败')

            teacher.act_click_favorite()
            self.assertTrue(teacher.is_favorite_for_teacher(), '点击关注教师按钮失败')

        if teacher.is_un_favorite_for_teacher() is True:
            teacher.act_click_favorite()
            self.assertTrue(teacher.is_favorite_for_teacher(), '点击关注教师按钮失败')

            teacher.act_click_cancel_favorite()
            self.assertTrue(teacher.is_un_favorite_for_teacher(), '点击取消关注教师按钮失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_教师点赞验证失败")
    def test_teacher_zan(self):
        """
        测试教师点赞
        :return:
        """

        self.teachers.act_click_random_teacher()

        teacher = models.Teacher(self.driver)
        if teacher.is_vote_for_teacher() is True:
            """已经点过赞，换一个教师试试"""

        teacher.act_click_vote_for_teacher()
        self.assertTrue(teacher.is_vote_for_teacher(), "验证教师点赞失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_随机进入同方向见识失败")
    def test_same_direction_teacher(self):
        """
        验证随机进入同方向讲师
        :return:
        """

        pass

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_随机进入金牌讲师失败")
    def test_gold_medal_teacher(self):
        """
        验证随机进入金牌讲师失败
        :return:
        """

        pass






