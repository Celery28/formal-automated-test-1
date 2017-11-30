# coding=utf-8
# 时间：2017-05-27
# 作者:李伟
# 主要内容：微社区冒烟用例
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import HTMLTestRunner
import unittest
# from bbs.test_UT import UT,UT1,UT3,UT2
# from bbs import test_UT
from imp import reload

from linux import test_UT
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class Suite():
    def test_suit_login(self):
        '''
        验证选课
        :return:
        '''
        suite=unittest.TestSuite()
        suite.addTest(unittest.makeSuite(test_UT.UT))
        suite.addTest(unittest.makeSuite(test_UT.UT1))
        suite.addTest(unittest.makeSuite(test_UT.UT2))
        suite.addTest(unittest.makeSuite(test_UT.UT3))
        # suite.addTest(UT('test_sign'))
        # suite.addTest(UT1('test_teacher'))
        # suite.addTest(UT1('test_course'))
        # suite.addTest(UT1('test_recycle'))
        file_name="./report1.html"
        file1=open(file_name,'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=file1,title=u'KGC冒烟用例',description=u'微社区测试报告')
        runner.run(suite)
if __name__=="__main__":
    Suite().test_suit_login()