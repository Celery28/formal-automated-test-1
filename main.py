#!/usr/bin/env python3
# _._ coding:utf-8 _._

"""
运行测试用例，形成测试报告

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""

import sys
import os
import time
import cases
import unittest
import getopt
from lib import unittest_
from lib.unittest_.runner import HTMLTestRunner

run_path = os.path.split(os.path.realpath(__file__))[0]
opts, args = getopt.getopt(sys.argv[1:], 'e:')

environment = 'production'
# environment = 'pre-production'
# environment = 'development'
for key, value in opts:
    if '-e' == key:
        environment = value

unittest_.TestCase.set_environment(environment)

if __name__ == '__main__':

    testsuite = unittest.TestSuite()

    """
    课工场网站首页测试用例，【正式环境已通过，dev和test环境可以不用执行】
    """
    # 验证进入课程库、就业实训、岗位课、金牌讲师界面
    testsuite.addTest(cases.HomepageTestCase("test_act_courses"))
    testsuite.addTest(cases.HomepageTestCase("test_act_employment_base"))
    testsuite.addTest(cases.HomepageTestCase("test_act_job"))
    testsuite.addTest(cases.HomepageTestCase("test_act_teachers"))

    """
    课程库列表页测试用例【正式、test、dev环境已通过】
    """
    # 验证课程库列表课程数量
    testsuite.addTest(cases.CoursesTestCase("test_courses_number"))
    # 验证课程库列表课程方向、分类筛选
    testsuite.addTest(cases.CoursesTestCase("test_first_category"))
    testsuite.addTest(cases.CoursesTestCase("test_sub_category"))
    # 验证课程库列表最新最热、收费免费、课程难度过滤器
    testsuite.addTest(cases.CoursesTestCase("test_courses_sort"))
    testsuite.addTest((cases.CoursesTestCase("test_courses_price_filter")))
    testsuite.addTest(cases.CoursesTestCase("test_course_difficulty_level"))

    """
    课程详情页测试用例
    """
    # TODO: 关闭浏览器出现问题
    # 验证免费课程购买【正式、test、dev环境已通过】
    testsuite.addTest(cases.CourseTestCase('test_free_course_buy'))
    # # 验证收费课程购买
    # testsuite.addTest(cases.CourseTestCase('test_no_free_course_buy'))
    # # 验证课程关注【正式环境已经通过】
    # testsuite.addTest(cases.CourseTestCase('test_course_favorite'))
    # # 验证课程标签【正式环境已经通过】
    # testsuite.addTest(cases.CourseTestCase('test_course_tag'))
    # # 验证教师关注【正式环境已经通过】
    # testsuite.addTest(cases.CourseTestCase('test_teacher_favorite'))
    # # 验证教师点赞【正式环境已经通过】
    # testsuite.addTest(cases.CourseTestCase('test_teacher_vote'))
    # 验证打开教师详情页【正式环境已经通过】
    testsuite.addTest(cases.CourseTestCase('test_open_teacher'))

    """
    岗位列表页测试用例
    """
    # 证进入岗位课详情页【正式、test、dev环境已通过】
    testsuite.addTest(cases.PostCoursesTestCase("test_post_course"))

    """
    岗位课详情页测试用例【正式、test、dev环境已通过】
    """
    # 测试岗位课中随机进入课程详情页
    testsuite.addTest(cases.PostCourseTestCase("test_course_details_page"))

    """
    教师列表页测试用例【正式、test、dev环境已通过】
    """
    # 验证随机筛选教师方向
    testsuite.addTest(cases.TeachersTestCase("test_teachers_category"))
    # 随机进入教师详情页
    testsuite.addTest(cases.TeachersTestCase("test_teachers_page"))

    """
    教师详情页测试用例
    """
    # # 验证教师详情页关注功能
    # testsuite.addTest(cases.TeacherTestCase("test_teacher_details_favorite"))
    # # 验证教师点赞功能
    # testsuite.addTest(cases.TeacherTestCase("test_teacher_zan"))
    # # 验证随机进入同方向讲师
    # testsuite.addTest(cases.TeacherTestCase("test_same_direction_teacher"))
    # # 验证随机进入金牌讲师页面
    # testsuite.addTest(cases.TeacherTestCase("test_gold_medal_teacher"))

    """
    搜索页面用例
    """
    # 验证搜索课程\帖子\老师\学友是否有数据
    testsuite.addTest(cases.SearchTestCase("test_search_course"))
    testsuite.addTest(cases.SearchTestCase("test_search_post"))
    testsuite.addTest(cases.SearchTestCase("test_search_teacher"))
    testsuite.addTest(cases.SearchTestCase("test_search_student"))
    # 验证搜索课程随机进入课程详情页功能
    testsuite.addTest(cases.SearchTestCase("test_search_course_enter_course_details_page"))
    # 验证随机搜索课程随机进入课程标签页
    testsuite.addTest(cases.SearchTestCase("test_search_course_enter_label_details_page"))
    # # TODO: 这个用例有些问题，需要优化
    # # 验证搜索课程翻页功能
    # # testsuite.addTest(cases.SearchTestCase("test_search_course_flip_pages"))
    # # 验证搜索帖子随机进入帖子详情页
    # testsuite.addTest(cases.SearchTestCase("test_search_post_enter_post_details_page"))
    # # 验证搜索帖子随机进入板块详情页
    # testsuite.addTest(cases.SearchTestCase("test_search_post_enter_plate_details_page"))
    # # 验证搜索帖子进入个人主页
    # testsuite.addTest(cases.SearchTestCase("test_search_post_enter_homepage"))
    # # 验证搜索教师随机进入教师主页
    # testsuite.addTest(cases.SearchTestCase("test_search_teacher_enter_teacher_homepage"))
    # # 验证搜索学友随机进入个人主页
    # testsuite.addTest(cases.SearchTestCase("test_search_user_enter_homepage"))
    # # 验证搜索学友随机加关注按钮
    # # testsuite.addTest(cases.SearchTestCase(""))

    """
    系列课页面用例
    """
    # 测试系列课程数量
    testsuite.addTest(cases.SeriesCourseTestCase("test_series_course_number"))
    # 测试系列课随机进入某节课程
    testsuite.addTest(cases.SeriesCourseTestCase("test_series_course"))

    """
    个人中心页面
    """
    # 测试就业课随机点击开始学习，进入播放课程列表
    testsuite.addTest(cases.PersonalCenterTestCase("test_job_course_learning_status"))
    # 测试就业课随机点击已过期状态，弹出正确的提示语
    testsuite.addTest(cases.PersonalCenterTestCase("test_job_courses_expired"))
    # # 测试就业课-修改笔记功能
    # testsuite.addTest(cases.PersonalCenterTestCase("test_job_course_modify_notes"))
    # # 测试就业课列表，点击课程名称进入就业课详情页
    # testsuite.addTest(cases.PersonalCenterTestCase("test_job_course_details_page"))

    # runner = unittest.TextTestRunner()
    # runner.run(testsuite)

    report_path = os.path.join(run_path, 'report')
    now = time.strftime('%Y-%m-%d %H-%M-%S')

    filename = os.path.join(report_path, now + 'report.html')
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title='课程库测试结果',
                            description='测试报告.')
    runner.run(testsuite)
