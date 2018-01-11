#!/usr/bin/python3.5.0
# coding=utf-8
# 时间：2017-05-27
# 作者:李伟
# 主要内容：微社区冒烟用例，签到，回复，发帖，关注
from selenium import webdriver
import random
import time
import sys
import inspect
from pyvirtualdisplay import Display
display = Display(visible=0, size=(2880,1720))
display.start()


from selenium import webdriver
import random
import time
import sys
import inspect
# from bbs.test_UT import UT
# '/html/body/div[3]/div[3]/div[1]/div[1]/span/span'有中心后台的账号
#'/html/body/div[2]/div[3]/div[1]/div[1]/span/span'没有中心后台的账号

global driver
class bbs(object):
    # global driver
    def get_current_function_name(self):
        '''
        返回当前方法名
        :return:
        '''
        return inspect.stack()[1][3]
    def openC(self,url,Account,Password):
        '''
        登录
        :return:
        '''
        # try:
        global driver
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        try:
            driver.find_element_by_link_text('登录').click()
        except:
            driver.refresh()
            driver.find_element_by_xpath('//*[@id="m-login-info-box"]/a[1]').click()
        driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys(Account)
        driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys(Password)
        driver.find_element_by_id('login').click()
        driver.implicitly_wait(30)
        # except:
        #     driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
        #     return 'false'
    def sign(self,a):
        '''
        签到
        :return:
        '''
        #签到前的数
    # try:
        Front = int(driver.find_element_by_xpath(a).text)+1
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[1]/a').click()
        except:
            driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
            return 'fasle'
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        # 签到后的数
        try:
            driver.find_element_by_link_text('关闭').click()
        except:
            Back = int(driver.find_element_by_xpath(a).text)
        if '%s'%Front == '%s'%Back:
            return 'true'
        else:
            driver.save_screenshot("test_%s.png" %(bbs().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
        #     return '代码有错false'
    # def Selected(self):
    #     '''
    #     随机选帖，随机点击回复，进行回复
    #     :return:
    #     '''
    #     try:
    #         driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/h2/span[6]/a').click()
    #
    #         #a楼层总数
    #         a = driver.find_elements_by_xpath('//*[@id="treeNav"]/li')
    #         b = random.randint(1,len(a))
    #         # driver.find_element_by_xpath('//*[@id="treeNav"]/li[%s]'%b).click()
    #         # #a总版块数
    #         # time.sleep(2)
    #         c = driver.find_elements_by_xpath('//*[@id="floor%s"]/div/ul/li'%b)
    #         if len(c)==2:
    #             d = random.randint(1, len(c))
    #             print (d)
    #         else:
    #             d = 1
    #         driver.find_element_by_xpath('//*[@id="floor%s"]/div/ul/li[%s]/div/div[2]/strong/a'%(b,d)).click()
    #         #随机进入标签
    #         e = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div[2]/a')
    #         print (len(e))
    #         f = random.randint(1,len(e))
    #         driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[%s]'%f).click()
    #         #随机进入分页
    #         try:
    #             fenye = driver.find_elements_by_xpath('//*[@id="yw1"]/li')
    #             g = random.randint(1,len(fenye))
    #             driver.find_element_by_xpath('//*[@id="yw1"]/li[%s]'%g).click()
    #         except:
    #             #随机选帖
    #             h = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div[3]/div[2]/ul/li')
    #             i = random.randint(1,len(h))
    #             text1=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[2]/ul/li[%s]/div[2]/div[1]/a' % i).text
    #         try:
    #             driver.find_element_by_link_text(text1).click()
    #
    #         except:
    #             h = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div[3]/div[2]/ul/li')
    #             i = random.randint(1, len(h))
    #             driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[2]/ul/li[%s]/div[2]/div[1]/a' % i).click()
    #             # 进入帖子
    #             driver.switch_to_window(driver.window_handles[-1])
    #             #随机选择回复
    #             a1 = driver.find_elements_by_xpath('//*[@id="yw0"]/ul/li')
    #             print('这是%s'%len(a1))
    #             b1 = random.randint(1,len(a1))
    #             print('这%s'%b1)
    #             driver.find_element_by_xpath('//*[@id="level%s"]/div[2]/div[4]/p/a[1]'%b1).click()
    #             time.sleep(2)
    #         try:
    #             driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[%s]/div[2]/div/div/form/textarea'%b1).send_keys('为课工场点赞')
    #         except:
    #             a1 = driver.find_elements_by_xpath('//*[@id="yw0"]/ul/li')
    #             b1 = random.randint(1, len(a1))
    #             try:
    #                 driver.find_element_by_xpath('//*[@id="level%s"]/div[2]/div[4]/p/a[1]'%b1).click()
    #                 time.sleep(1)
    #                 driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[%s]/div[2]/div/div/form/textarea' % b1).send_keys( '为课工场点赞')
    #             except:
    #                 a1 = driver.find_elements_by_xpath('//*[@id="yw0"]/ul/li')
    #                 b1 = random.randint(1, len(a1))
    #                 driver.find_element_by_xpath('//*[@id="level%s"]/div[2]/div[4]/p/a[1]' % b1).click()
    #                 time.sleep(1)
    #                 driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[%s]/div[2]/div/div/form/textarea' % b1).send_keys('为课工场点赞')
    #             driver.find_element_by_link_text('提交').click()
    #         time.sleep(5)
    #         # 断言
    #         count=driver.find_element_by_xpath('//*[@id="all-evalue"]/span').text
    #         driver.refresh()
    #         count1=driver.find_element_by_xpath('//*[@id="all-evalue"]/span').text
    #         print('%s%s'%(count[1:2],count1[1:2]))
    #         if count[1:2] < count1[1:2]:
    #             return 'true'
    #         else:
    #             driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
    #             return 'false'
    #     except:
    #         driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
    #         return 'false'


    def post(self):
        '''
        发帖
        :return:
        '''
        # try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/h2/span[6]/a').click()
        # a楼层总数
        a = driver.find_elements_by_xpath('//*[@id="treeNav"]/li')
        b = random.randint(1, len(a))
        print(b)
        # driver.find_element_by_xpath('//*[@id="treeNav"]/li[%s]'%b).click()
        # #a总版块数
        # time.sleep(2)
        c = driver.find_elements_by_xpath('//*[@id="floor%s"]/div/ul/li' % b)
        d = random.randint(1, len(c))
        print(d)
        driver.find_element_by_xpath('//*[@id="floor%s"]/div/ul/li[%s]/div/div[2]/strong/a' % (b, d)).click()
        # 随机进入标签
        e = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div[2]/a')
        f = random.randint(1, len(e)-1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/a[%s]' % f).click()
        # 随机进入分页
        try:
            fenye = driver.find_elements_by_xpath('//*[@id="yw1"]/li')
            g = random.randint(2, len(fenye) - 2)
            driver.find_element_by_xpath('//*[@id="yw1"]/li[%s]' % g).click()
        finally:
            driver.find_element_by_link_text('我要发帖').click()
            driver.find_element_by_id('postTitle').send_keys('为课工场点赞')
            #随机分类
            a = driver.find_elements_by_xpath('//*[@id="product"]/option')
            b = random.randint(1,len(a))
            driver.find_element_by_id('product').click()
            driver.find_element_by_xpath('//*[@id="product"]/option[%s]'%b).click()
            driver.switch_to_frame('ueditor_0')
            driver.find_element_by_xpath('/html/body').send_keys('为课工场点赞')
            driver.switch_to_default_content()
            driver.find_element_by_id('post').click()
            # 断言
            dy=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/h2').text
            if '%s'%dy=='为课工场点赞':
                return 'true'
            else:
                return 'false'
        # except:
        #     driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
        #     return '代码有错false'
    def follow1(self):
        '''
        关注
        :return:
        '''
        # try:
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/h2/span[6]/a').click()
        # a楼层总数
        a = driver.find_elements_by_xpath('//*[@id="treeNav"]/li')
        b = random.randint(1, len(a))
        print(b)
        # driver.find_element_by_xpath('//*[@id="treeNav"]/li[%s]'%b).click()
        # #a总版块数
        # time.sleep(2)
        c = driver.find_elements_by_xpath('//*[@id="floor%s"]/div/ul/li' % b)
        d = random.randint(1, len(c))
        print(d)
        driver.find_element_by_xpath('//*[@id="floor%s"]/div/ul/li[%s]/div/div[2]/strong/a' % (b, d)).click()
        try:
            driver.find_element_by_xpath('//*[@id="header-qd-tip"]/a[2]').click()
        finally:
            dy=driver.find_element_by_xpath('/html/body/div[2]/div/a').text
        print('点击前'+dy)
        driver.find_element_by_xpath('/html/body/div[2]/div/a').click()
        time.sleep(2)
        driver.refresh()
        dy1=driver.find_element_by_xpath('/html/body/div[2]/div/a').text
        print('点击后'+dy1)
        if '%s'%dy=='关注'and '%s'%dy1=='已关注':
            return 'true'
        elif '%s'%dy=='已关注' and '%s'%dy1=='关注':
            return 'true'
        else:
            driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("test_%s.png" % (bbs().get_current_function_name()))
        #     return '代码有错false'
    def close(self):
        driver.quit()
#
if __name__=='__main__':

    # bbs().Selected()
    bbs().openC('http://www.kgc.dev.cn/bbs','13581917428','123456')
    print(bbs().follow1())
