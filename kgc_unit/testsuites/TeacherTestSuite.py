from unittest import TestSuite

from kgc_unit import testcases

"""
教师测试套件

:author chaoyang.li <chaoyang.li@kgc.cn>
"""

TeacherTestSuite = TestSuite()

# 教师列表页测试用例【正式、test、dev环境已通过】

# 验证随机筛选教师方向
TeacherTestSuite.addTest(testcases.TeachersTestCase("test_teachers_category"))

# 随机进入教师详情页
TeacherTestSuite.addTest(testcases.TeachersTestCase("test_teachers_page"))

# 教师详情页测试用例

# 验证教师详情页关注功能
TeacherTestSuite.addTest(testcases.TeacherTestCase("test_teacher_details_favorite"))

# 验证教师点赞功能
TeacherTestSuite.addTest(testcases.TeacherTestCase("test_teacher_zan"))

# 验证随机进入同方向讲师
TeacherTestSuite.addTest(testcases.TeacherTestCase("test_same_direction_teacher"))

# 验证随机进入金牌讲师页面
TeacherTestSuite.addTest(testcases.TeacherTestCase("test_gold_medal_teacher"))
