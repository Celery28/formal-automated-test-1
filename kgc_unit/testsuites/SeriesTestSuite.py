from unittest import TestSuite

from kgc_unit import testcases

"""
系列课测试套件

:author chaoyang.li <chaoyang.li@kgc.cn>
"""

SeriesTestSuite = TestSuite()

# 测试系列课程数量
SeriesTestSuite.addTest(testcases.SeriesCourseTestCase("test_series_course_number"))

# 测试系列课随机进入某节课程
SeriesTestSuite.addTest(testcases.SeriesCourseTestCase("test_series_course"))
