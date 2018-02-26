from kgc_unit.testsuites import TestSuite

from kgc_unit import testcases

"""
首页测试套件

:author chaoyang.li <chaoyang.li@kgc.cn>
"""


class HomepageTestSuite(TestSuite):

    def suites(self):
        # 【正式环境已通过，dev和test环境可以不用执行】
        # 验证进入课程库、就业实训、岗位课、金牌讲师界面

        self.addTest(testcases.HomepageTestCase("test_act_courses"))
        self.addTest(testcases.HomepageTestCase("test_act_employment_base"))
        self.addTest(testcases.HomepageTestCase("test_act_job"))
        self.addTest(testcases.HomepageTestCase("test_act_teachers"))
