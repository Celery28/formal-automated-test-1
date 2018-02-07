from unittest import TestSuite

from kgc_unit import testcases

"""
岗位课测试套件

:author chaoyang.li <chaoyang.li@kgc.cn>
"""

PostCourseTestSuite = TestSuite()

# 【正式、test、dev环境已通过】

# 验证进入岗位课详情页
PostCourseTestSuite.addTest(testcases.PostCoursesTestCase("test_post_course"))

# 测试岗位课中随机进入课程详情页
PostCourseTestSuite.addTest(testcases.PostCourseTestCase("test_course_details_page"))
