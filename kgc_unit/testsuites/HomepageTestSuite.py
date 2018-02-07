from unittest import TestSuite

from kgc_unit import testcases

"""
首页测试套件

:author chaoyang.li <chaoyang.li@kgc.cn>
"""

HomepageTestSuite = TestSuite()

# 【正式环境已通过，dev和test环境可以不用执行】
# 验证进入课程库、就业实训、岗位课、金牌讲师界面
HomepageTestSuite.addTest(testcases.HomepageTestCase("test_act_courses"))
HomepageTestSuite.addTest(testcases.HomepageTestCase("test_act_employment_base"))
HomepageTestSuite.addTest(testcases.HomepageTestCase("test_act_job"))
HomepageTestSuite.addTest(testcases.HomepageTestCase("test_act_teachers"))
