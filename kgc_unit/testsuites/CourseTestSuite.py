from unittest import TestSuite

from kgc_unit import testcases

"""
课程测试套件

:author chaoyang.li <chaoyang.li@kgc.cn>
"""

CourseTestSuite = TestSuite()

# 【正式、test、dev环境已通过】

# 验证课程库列表课程数量
CourseTestSuite.addTest(testcases.CoursesTestCase("test_courses_number"))

# 验证课程库列表课程方向、分类筛选
CourseTestSuite.addTest(testcases.CoursesTestCase("test_first_category"))
CourseTestSuite.addTest(testcases.CoursesTestCase("test_sub_category"))

# 验证课程库列表最新最热、收费免费、课程难度过滤器
CourseTestSuite.addTest(testcases.CoursesTestCase("test_courses_sort"))
CourseTestSuite.addTest(testcases.CoursesTestCase("test_courses_price_filter"))
CourseTestSuite.addTest(testcases.CoursesTestCase("test_course_difficulty_level"))

# TODO: 关闭浏览器出现问题
# 验证免费课程购买【正式、test、dev环境已通过】
CourseTestSuite.addTest(testcases.CourseTestCase('test_free_course_buy'))

# 验证收费课程购买
CourseTestSuite.addTest(testcases.CourseTestCase('test_no_free_course_buy'))

# 验证课程关注【正式环境已经通过】
CourseTestSuite.addTest(testcases.CourseTestCase('test_course_favorite'))

# 验证课程标签【正式环境已经通过】
CourseTestSuite.addTest(testcases.CourseTestCase('test_course_tag'))

# 验证教师关注【正式环境已经通过】
CourseTestSuite.addTest(testcases.CourseTestCase('test_teacher_favorite'))

# 验证教师点赞【正式环境已经通过】
CourseTestSuite.addTest(testcases.CourseTestCase('test_teacher_vote'))

# 验证打开教师详情页【正式环境已经通过】
CourseTestSuite.addTest(testcases.CourseTestCase('test_open_teacher'))
