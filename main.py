#!/usr/bin/env python3
# _._ coding:utf-8 _._

"""
运行测试用例，形成测试报告

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""

import os
import time

import cases
import unittest
from lib.unittest_.runner import HTMLTestRunner
# from linux import test_UT

run_path = os.path.split(os.path.realpath(__file__))[0]

if __name__ == '__main__':

    testsuite = unittest.TestSuite()

    """
    课工场网站首页测试用例
    """
    # # 验证进入课程库界面
    # testsuite.addTest(cases.HomepageTestCase("test_act_courses"))
    # # 验证进入就业实训界面
    # testsuite.addTest(cases.HomepageTestCase("test_act_employment_base"))
    # # 验证进入岗位课界面
    # testsuite.addTest(cases.HomepageTestCase("test_act_job"))
    # # 验证进入金牌讲师界面
    # testsuite.addTest(cases.HomepageTestCase("test_act_teachers"))

    """
    课程库列表页测试用例
    """
    # # 验证课程库列表课程数量
    # testsuite.addTest(cases.CoursesTestCase("test_courses_number"))
    # # 验证课程库列表课程方向筛选
    # testsuite.addTest(cases.CoursesTestCase("test_first_category"))
    # # 验证课程库列表课程分类筛选
    # testsuite.addTest(cases.CoursesTestCase("test_sub_category"))
    # # 验证课程库列表筛选课程最新最热状态
    # testsuite.addTest(cases.CoursesTestCase("test_courses_sort"))
    # # 验证课程库收费与免费过滤器
    # testsuite.addTest((cases.CoursesTestCase("test_courses_price_filter")))
    # # 验证课程库列表筛选课程难度
    # testsuite.addTest(cases.CoursesTestCase("test_course_difficulty_level"))

    """
    李伟用例
    """
    # testsuite.addTest(unittest.makeSuite(test_UT.UT))
    # testsuite.addTest(unittest.makeSuite(test_UT.UT1))
    # testsuite.addTest(unittest.makeSuite(test_UT.UT2))
    # testsuite.addTest(unittest.makeSuite(test_UT.UT3))

    """
    课程详情页测试用例
    """
    # # 验证免费课程购买
    # testsuite.addTest(cases.CourseTestCase('test_free_course_buy'))
    # # 验证收费课程购买
    # testsuite.addTest(cases.CourseTestCase('test_no_free_course_buy'))
    # # 验证课程关注
    # testsuite.addTest(cases.CourseTestCase('test_course_favorite'))
    # # 验证课程标签
    # testsuite.addTest(cases.CourseTestCase('test_course_tag'))
    # # 验证教师关注
    # testsuite.addTest(cases.CourseTestCase('test_teacher_favorite'))
    # # 验证教师点赞
    # testsuite.addTest(cases.CourseTestCase('test_teacher_vote'))
    # # 验证打开教师详情页
    # testsuite.addTest(cases.CourseTestCase('test_open_teacher'))

    """
    岗位列表页测试用例
    """
    # # 证进入岗位课详情页
    # testsuite.addTest(cases.PostCoursesTestCase("test_post_course"))
    # # 验证进入下一课
    # # testsuite.addTest(cases.PostCoursesTestCase("test_next_course"))

    """
    教师列表页测试用例
    """
    # # 验证随机筛选教师方向
    # testsuite.addTest(cases.TeachersTestCase("test_teachers_category"))
    # # 随机进入教师详情页
    # testsuite.addTest(cases.TeachersTestCase("test_teachers_page"))

    """
    教师详情页测试用例
    """
    # 验证教师详情页关注功能
    testsuite.addTest(cases.TeacherTestCase("test_teacher_details_favorite"))
    # 验证教师点赞功能
    # ？ 未开发完成，循环功能暂未开发
    testsuite.addTest(cases.TeacherTestCase("test_teacher_zan"))
    # # 验证随机进入同方向讲师
    # testsuite.addTest(cases.TeacherTestCase("test_same_direction_teacher"))
    # # 验证随机进入金牌讲师页面
    # testsuite.addTest(cases.TeacherTestCase("test_gold_medal_teacher"))

    runner = unittest.TextTestRunner()
    runner.run(testsuite)

    # report_path = os.path.join(run_path, 'report')
    # now = time.strftime('%Y-%m-%d %H-%M-%S')
    #
    # filename = os.path.join(report_path, now + 'report.html')
    # fp = open(filename, 'wb')
    #
    # runner = HTMLTestRunner(stream=fp,
    #                         title='课程库测试结果',
    #                         description='测试报告.')
    # runner.run(testsuite)
