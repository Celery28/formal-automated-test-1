from unittest import TestSuite

from kgc_unit import testcases

"""
搜索测试套件

:author chaoyang.li <chaoyang.li@kgc.cn>
"""

SearchTestSuite = TestSuite()

# 搜索页面用例

# 验证搜索课程\帖子\老师\学友是否有数据
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_course"))
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_post"))
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_teacher"))
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_student"))

# 验证搜索课程随机进入课程详情页功能
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_course_enter_course_details_page"))

# # 验证随机搜索课程随机进入课程标签页
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_course_enter_label_details_page"))

# # TODO: 这个用例有些问题，需要优化
# 验证搜索课程翻页功能
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_course_flip_pages"))

# 验证搜索帖子随机进入帖子详情页
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_post_enter_post_details_page"))

# 验证搜索帖子随机进入板块详情页
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_post_enter_plate_details_page"))

# 验证搜索帖子进入个人主页
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_post_enter_homepage"))

# 验证搜索教师随机进入教师主页
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_teacher_enter_teacher_homepage"))

# 验证搜索学友随机进入个人主页
SearchTestSuite.addTest(testcases.SearchTestCase("test_search_user_enter_homepage"))

# 验证搜索学友随机加关注按钮
# SearchTestSuite.addTest(testcases.SearchTestCase(""))
