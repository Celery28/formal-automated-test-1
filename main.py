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
parser.add_argument('-r', '--report', action="store_true", help='生成HTML测试报告')
parser.add_argument('-ss', '--suites', default=[], nargs='*', help='设置运行的测试套件，若不设置则执行所有套件')

opts = parser.parse_args()

testcases.TestCase.set_environment(opts.environment)  # value of: development production pre-production
all_test_suites = {_suite[:-9].lower(): _suite for _suite in testsuites.__dict__ if 'TestSuite' in _suite}

if __name__ == '__main__':

    suite = unittest.TestSuite()

    for suite_name in opts.suites or all_test_suites.keys():
        if suite_name.lower() not in all_test_suites.keys():
            raise NameError("无法找到对应的测试套件：{0}".format(suite_name))

        suite.addTests(testsuites.__dict__[all_test_suites[suite_name.lower()]])

    if opts.report is False:
        runner = unittest.TextTestRunner()
    else:
        report_path = os.path.join(run_path, 'report')
        now = time.strftime('%Y-%m-%d %H-%M-%S')

        filename = os.path.join(report_path, now + 'report.html')
        fp = open(filename, 'wb')

        runner = HTMLTestRunner(stream=fp, title='课程库测试结果', description='测试报告.')

    runner.run(suite)
