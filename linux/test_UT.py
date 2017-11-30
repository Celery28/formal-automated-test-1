# coding=utf-8
# 时间：2017-05-27
# 作者:李伟
# 主要内容：微社区;个人中心；商城冒烟用例
from selenium import webdriver
from linux import bbsj,PersonalC,shop,Training

from unittest import TestCase
import sys
class UT(TestCase):
    def setUp(self):
        global Basics
        Basics=bbsj.bbs()
        Basics.openC('http://www.kgc.cn/bbs','502120020@qq.com','910227')
    def tearDown(self):
        global Basics
        Basics = bbsj.bbs()
        Basics.close()
    def test_sign(self):
        u'''签到'''
        count=Basics.sign('/html/body/div[2]/div[3]/div[1]/div[1]/span/span')
        print (count)
        self.assertEqual(count,'true','测试通过')
    # def test_Selected(self):
    #     u'''回复帖子'''
    #     selected=Basics.Selected()
    #     self.assertEqual(selected,'true','测试通过')
    def test_post(self):
        u'''发帖'''
        post=Basics.post()
        self.assertEqual(post,'true','测试通过')
    def test_follow(self):
        u'''关注'''
        follow=Basics.follow()
        self.assertEqual(follow,'true','测试通过')
class UT1(TestCase):
    def setUp(self):
        global Person
        Person=PersonalC.PersonalC()
        Person.openC('http://www.kgc.cn/','502120020@qq.com','910227')
    def tearDown(self):
        global Person
        Person = PersonalC.PersonalC()
        Person.close()
    def test_mycourse(self):
        u'''我的课程'''
        mycourse=Person.mycourse()
        self.assertEqual(mycourse,'true','测试通过')
    def test_teacher(self):
        u'''关注教师'''
        teacher=Person.teacher()
        self.assertEqual(teacher,'true','测试通过')
    def test_course(self):
        u'''关注的课程'''
        course=Person.course()
        self.assertEqual(course,'true','测试通过')
    def test_recycle(self):
        u'''回收站'''
        recycle=Person.recycle()
        self.assertEqual(recycle,'true','测试通过')
    def test_dynamic(self):
        u'''动态'''
        dynamic=Person.dynamic()
        self.assertEqual(dynamic,'true','测试通过')
    def test_Questions(self):
        u'''题库'''
        Questions=Person.Questions()
        self.assertEqual(Questions,'true','测试通过')
    def test_Community(self):
        u'''个人中心发帖'''
        Community=Person.Community()
        self.assertEqual(Community,'true','测试通过')
    def test_Community_Reply(self):
        u'''微社区回帖'''
        Community_Reply=Person.Community_Reply()
        self.assertEqual(Community_Reply,'true','测试通过')
    def test_Community_Post(self):
        u'''关注帖子'''
        Community_Post=Person.Community_Post()
        self.assertEqual(Community_Post,'true','测试通过')
    def test_Community_follow(self):
        u'''关注板块'''
        Community_follow=Person.Community_follow()
        self.assertEqual(Community_follow,'true','测试通过')
    def test_task(self):
        u'''新手任务'''
        task=Person.task()
        self.assertEqual(task,'true','测试通过')
    def test_wallet(self):
        u'''钱包'''
        wallet=Person.wallet()
        self.assertEqual(wallet,'true','测试通过')
    def test_Set_up1(self):
        u'''修改昵称'''
        Set_up1=Person.Set_up1()
        self.assertEqual(Set_up1,'true','测试通过')
    def test_Set_up2(self):
        u'''修改密码，手机，邮箱'''
        Set_up2=Person.Set_up2()
        self.assertEqual(Set_up2,'true','测试通过')
    def test_Set_up3(self):
        u'''修改个人资料'''
        Set_up3=Person.Set_up3()
        self.assertEqual(Set_up3,'true','测试通过')
    def test_Set_up4(self):
        u'''头像页面验证'''
        Set_up4=Person.Set_up4()
        self.assertEqual(Set_up4,'true','测试通过')
# class UT2(TestCase):
#     def setUp(self):
#         global Shop
#         Shop=shop.shop()
#         Shop.openC('http://www.kgc.cn/goods','502120020@qq.com','910227')
#     def tearDown(self):
#         Shop = shop.shop()
#         Shop.close()
#     def test_Buy(self):
#         u'''商城购买'''
#         buy=Shop.Buy()
#         self.assertEqual(buy,'true','测试通过')
class UT3(TestCase):
    def setUp(self):
        global training
        training=Training.Training()
        training.openC('http://www.kgc.cn/','502120020@qq.com','910227')
    def tearDown(self):
        training.close()
    #     导航栏链接禁用
    # def test_Navigation(self):
    #     u'''就业实训导航栏跳转'''
    #     Navigation=training.Navigation()
    #     self.assertEqual(Navigation,'true','测试通过')
    def test_look(self):
        u'''观看初级，高级课程'''
        look=training.look()
        self.assertEqual(look,'true','测试通过')

if __name__=='__main__':
    a=UT()
    a.setUp()
    a.test_sign()
    a.tearDown()