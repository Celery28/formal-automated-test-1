#!/usr/bin/env python3
# _._ coding:utf-8 _._

"""
运行测试用例，形成测试报告

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""

import os
import time
import unittest
import argparse

from kgc_unit import testcases
from kgc_unit import testsuites
from common.unittest_.runner import HTMLTestRunner

run_path = os.path.split(os.path.realpath(__file__))[0]

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--environment', default='development', help='运行的测试环境，默认为：development。可选值：development pre-production production')
parser.add_argument('-s', '--console', action="store_true", help='使用控制台输出')
parser.add_argument('-ss', '--suites', default=[], nargs='*', help='设置运行的测试套件，若不设置则执行所有套件')

opts = parser.parse_args()

testcases.TestCase.set_environment(opts.environment)  # value of: development production pre-production
default_test_suites = ['homepage', 'course', 'personalCenter', 'postCourse', 'search', 'series', 'teacher']

if __name__ == '__main__':

    suite = unittest.TestSuite()

    for suite_name in opts.suites or default_test_suites:
        suite_real_name = suite_name[0].upper() + suite_name[1:] + "TestSuite"

        if suite_real_name not in testsuites.__dict__:
            raise NameError("无法找到对应的测试套件：{0}".format(suite_real_name))

        suite.addTests(testsuites.__dict__[suite_real_name])

    if opts.console is True:
        runner = unittest.TextTestRunner()
    else:
        report_path = os.path.join(run_path, 'report')
        now = time.strftime('%Y-%m-%d %H-%M-%S')

        filename = os.path.join(report_path, now + 'report.html')
        fp = open(filename, 'wb')

        runner = HTMLTestRunner(stream=fp, title='课程库测试结果', description='测试报告.')

    runner.run(suite)
