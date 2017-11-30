# coding=utf-8
# 时间：2017-6-13
# 作者:李伟
# 主要内容：个人中心课程
from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import inspect
from pyvirtualdisplay import Display
display = Display(visible=0, size=(2880,1720))
display.start()

class PersonalC(object):
    def get_current_function_name(self):
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
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys(Account)
        driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys(Password)
        driver.find_element_by_id('login').click()
        driver.implicitly_wait(30)
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'

    def mycourse(self):
        '''
        我的课程
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[2]/a').click()
        #随机选择学习状态
        state=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/p')
        ActionChains(driver).move_to_element(state).perform()
        number2=random.randint(1,3)
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/dl/dt[%s]/a'%number2).click()
        count=len(driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/a'))
        # 分类随机
        number=random.randint(1,count)
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/a[%s]'%number).click()
        # 课程随机
        count1=len(driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li'))
        number1=random.randint(1,count1)
        # 获取课程名
        try:
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[%s]/div[2]/div[1]/div/label[1]'%number1).text
        except:
            number1=random.randint(1,count1)
        name=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[%s]/div[2]/div[1]/a'%number1).text
        # 点击课程图片
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[%s]/div[2]/a/img'%number1).click()
        driver.switch_to_window(driver.window_handles[-1])
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/a[3]').click()
            name1=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/h2').text
        except:
            name1=driver.find_element_by_xpath('//*[@id="title"]/h2').text
        driver.switch_to_window(driver.window_handles[0])
        # 点击标题
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[%s]/div[2]/div[1]/a' % number1).click()
        driver.switch_to_window(driver.window_handles[-1])
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/a[3]').click()
            name2=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/h2').text
        except:
            name2=driver.find_element_by_xpath('//*[@id="title"]/h2').text
        driver.switch_to_window(driver.window_handles[0])
        # 按钮文字
        title=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[%s]/div[2]/div[2]/a'%number1).text
        if title !='开始学习':
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[%s]/div[2]/div[2]/a'%number1).click()
            driver.switch_to_window(driver.window_handles[-1])
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/a[3]').click()
                name3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/h2').text
            except:
                name3 = driver.find_element_by_xpath('//*[@id="title"]/h2').text
        else:
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[%s]/div[2]/div[2]/a'%number1).click()
            time.sleep(3)
            try:
                name3 =driver.find_element_by_xpath('//*[@id="player-right"]/div/div[1]/h1').text

            except:
                time.sleep(3)

                name3 =driver.find_element_by_xpath('//*[@id="player-right"]/div/div[1]/h1').text

            name3=driver.find_element_by_xpath('//*[@id="player-right"]/div/div[1]/h1').text
        print(name,name1,name2,name3)
        return 'true'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def teacher(self):
        '''
        关注教师：关注及取消关注
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[2]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[1]/span/a[2]').click()
        name=driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/p[1]/a[1]/span').text
        driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/p[1]/a[1]/span').click()
        # 教师详情页的教师名称
        name1=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/p[1]/span').text
        #关注按钮状态
        follow=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]').text
        if follow[0:3]=='已关注' and name==name1:
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]').click()
            time.sleep(2)
            driver.back()
        # 首个教师名称
            name2=driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/p[1]/a[1]/span').text
            if name!=name2:
                driver.forward()
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]').click()
                time.sleep(2)
                driver.back()
                name3=driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/p[1]/a[1]/span').text
                if name==name3:

                    return 'true'
                else:
                    driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                    return 'false'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'

    def course(self):
        '''
        关注的课程
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[2]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[1]/span/a[3]').click()
        number = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/a')
        #         选取分类
        number1 = random.randint(1, len(number))
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/a[%s]' % number1).click()
        #         获取课程数
        count = driver.find_elements_by_xpath('//*[@id="yw0"]/ul/li')
        if len(count) > 1:
            # 随机获取课程
            count1 = random.randint(1, len(count) - 1)
            name = driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[%s]/ div[2] / div / h2 / a' % count1).text
            driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[%s]' % count1).click()
            driver.switch_to_window(driver.window_handles[-1])
            name1 = driver.find_element_by_xpath('//*[@id="title"]/h2').text
            if '%s' % name == '%s' % name1:
                try:
                    time.sleep(3)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[5]/div[3]/div/a').click()

                except:
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[5]/div[3]/div/a').click()
                driver.switch_to_window(driver.window_handles[0])
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[3]').click()
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/a[%s]' % number1).click()
                name2 = driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[%s]' % count1).text
                if '%s' % name != '%s' % name2:
                    driver.switch_to_window(driver.window_handles[-1])
                    driver.find_element_by_id('favorites').click()
                    driver.switch_to_window(driver.window_handles[0])
                    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/a[1]').click()
                    name3 = driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[1]/div[2]/div/h2/a').text
                    if '%s' % name == '%s' % name3:
                        return 'true'
                    else:
                        driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                        return 'false'
                else:
                    driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                    return 'false'
            else:
                driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                return 'false'
        elif len(count) == 1:
            name = driver.find_element_by_xpath('//*[@id="yw0"]/ul/li/div[2]/div/h2/a').text
            driver.find_element_by_xpath('//*[@id="yw0"]/ul/li/div[2]/div/h2/a').click()
            driver.switch_to_window(driver.window_handles[-1])
            name1 = driver.find_element_by_xpath('//*[@id="title"]/h2').text
            if '%s' % name == '%s' % name1:
                try:
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/a[2]').click()
                except:
                    driver.find_element_by_xpath('//*[@id="title"]/div/div/div[2]/a').click()
                driver.switch_to_window(driver.window_handles[0])
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/a[%s]' % number1).click()
                driver.find_elements_by_xpath('//*[@id="yw0"]/ul/li')
                driver.switch_to_window(driver.window_handles[-1])
                driver.find_element_by_xpath('//*[@id="title"]/div/div/div[2]/a').click()
                driver.switch_to_window(driver.window_handles[0])
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[3]').click()
                name2 = driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[1]/div[2]/div/h2/a').text
                if '%s' % name == '%s' % name2:
                    return 'true'
                else:
                    driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                    return 'false'
            else:
                driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                return 'false'
        else:
            # 分类名
            FenLei = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/a[%s]' % number1).text
            driver.find_element_by_xpath('//*[@id="yw0"]/ul/span/div/a').click()
            FenLei1 = driver.find_element_by_xpath('//*[@id="rightContent"]/div[1]/div[1]/strong').text
            if FenLei == FenLei1[1:6]:
                driver.find_element_by_xpath('//*[@id="yw1"]/ul/li[1]/div[1]/a/img').click()
                driver.switch_to_window(driver.window_handles[-1])
                try:
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/a[2]').click()
                except:
                    driver.find_element_by_xpath('//*[@id="favorites"]').click()
                name = driver.find_element_by_xpath('//*[@id="title"]/h2').text
                driver.switch_to_window(driver.window_handles[0])
                driver.back()
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[3]').click()
                name1 = driver.find_element_by_xpath('//*[@id="yw0"]/ul/li[1]/div[2]/div/h2/a').text
                if '%s' % name == '%s' % name1:
                    return 'true'
                else:
                    driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                    return 'false'
            else:
                driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def recycle(self):
        '''
        课程回收站：删除及恢复
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[2]/a').click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div[2]/div[1]/div')).perform()
        # ActionChains.move_to_element(driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div[2]/div[1]/div/label[2]')).perform()
        text1=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/div[1]/a').text
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div[2]/div[1]/div/label[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[2]/div/p[2]/a[1]').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[1]/span/a[4]').click()
        text2=driver.find_element_by_xpath('//*[@id="purchase-course-grid"]/ul/li[1]/div[2]/div/h2/a').text
        if text1==text2:
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/a').click()
            driver.find_element_by_xpath('//*[@id="purchase-course-grid"]/ul/li[1]/div[1]/div[2]').click()
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/a').click()
            time.sleep(3)
            text3=driver.find_element_by_xpath('//*[@id="purchase-course-grid"]/ul/li[1]/div[2]/div/h2/a').text
            if text2!=text3:
                return 'true'
            else:
                return 'false1'
        else:
            return 'false2'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def dynamic(self):
        '''
        动态
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_link_text('动态').click()
        text1=driver.find_element_by_link_text('最新动态').text
        if text1=='最新动态':
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def Questions(self):
        '''
        题库
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[4]/a').click()
        #个人中心题目名称
        js = "var q=document.documentElement.scrollTop=300"
        driver.execute_script(js)
        count1=random.randint(1,6)
        text1=driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[%s]/div[1]/a'%count1).text
        driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[%s]/div[1]/a'%count1).click()
        #题库题目名称
        text2=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/h2/pre').text
        driver.back()
        time.sleep(2)
        # name1=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/span/a[2]').text
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/span/a[2]').click()
        # count=driver.find_elements_by_xpath('//*[@id="user-care-grid"]/ul/li')
        # count1=random.randint(0,len(count))
        # 个人中心关注题目名称
        text3=driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[1]/div[1]/a').text
        driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[1]/div[1]/a').click()
        # 题库题目名称
        text4=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/h2/pre').text
        driver.find_element_by_id('question_guanzhu').click()
        driver.back()
        text5=driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[1]/div[1]/a').text
        if '%s'%text5!='%s'%text4:
            driver.forward()
        else:
            return 'false'
        driver.find_element_by_id('question_guanzhu').click()
        driver.back()
        text6=driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[1]/div[1]/a').text
        if '%s'%text1[0:4]=='%s'%text2[0:4] and '%s'%text3[0:4]=='%s'%text4[0:4] and '%s'%text6[0:4]=='%s'%text3[0:4]:
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def Community(self):
        '''
        发帖
        :return:
        '''
        try:
            driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
            driver.find_element_by_xpath('//*[@id="qd-nav"]/li[5]/a').click()
            count=driver.find_elements_by_xpath('//*[@id="user-care-grid"]/ul/li')
            count1=random.randint(1,len(count))
            # 个人中心发表帖子的名称
            text1=driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[%s]/div[2]/h2/a[2]'%count1).text
            driver.find_element_by_xpath('//*[@id="user-care-grid"]/ul/li[%s]/div[2]/h2/a[2]'%count1).click()
            driver.switch_to_window(driver.window_handles[-1])
            # 微社区帖子名称
            text2=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/h2').text
            if '%s'%text1[0:4]=='%s'%text2[0:4]:
                return 'true'
            else:
                driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                return 'false'
        except:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return '代码有错'
    def Community_Reply(self):
        '''
        回复帖子
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[5]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/span/a[2]').click()
        count = driver.find_elements_by_xpath('//*[@id="post-publish-grid"]/ul/li')
        count1 = random.randint(1, len(count))
        text1 = driver.find_element_by_xpath('//*[@id="post-publish-grid"]/ul/li[%s]/div[2]/h2/a[2]' % count1).text
        driver.find_element_by_xpath('//*[@id="post-publish-grid"]/ul/li[%s]/div[2]/h2/a[2]' % count1).click()
        driver.switch_to_window(driver.window_handles[-1])
        text2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/h2').text
        if '%s'%text1[0:3]=='%s'%text2[0:3]:
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def Community_Post(self):
        '''
        关注帖子
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[5]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[3]').click()
        text1 = driver.find_element_by_xpath('//*[@id="post-publish-grid"]/ul/li[1]/div[2]/h2/a[2]').text
        driver.find_element_by_xpath('//*[@id="post-publish-grid"]/ul/li[1]/div[2]/h2/a[2]').click()
        driver.switch_to_window(driver.window_handles[-1])
        text2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/h2').text
        if '%s' % text1[0:3] == '%s' % text2[0:3]:
            # 取消关注
            driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/a').click()
            driver.switch_to_window(driver.window_handles[0])
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[3]').click()
            text1 = driver.find_element_by_xpath('//*[@id="post-publish-grid"]/ul/li[1]/div[2]/h2/a[2]').text
            if '%s' % text1[0:3] != '%s' % text2[0:3]:
                # 关注
                driver.switch_to_window(driver.window_handles[-1])
                driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/a').click()
                driver.switch_to_window(driver.window_handles[0])
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[3]').click()
                text1 = driver.find_element_by_xpath('//*[@id="post-publish-grid"]/ul/li[1]/div[2]/h2/a[2]').text
                if '%s'%text1[0:3]=='%s'%text2[0:3]:
                    return 'true'
                else:
                    driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                    return 'false3'
            else:
                driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                return 'false2'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false1'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def Community_follow(self):
        '''
        关注板块
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[5]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[4]').click()
        text1=driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/h2/a').text
        driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/h2/a').click()
        driver.switch_to_window(driver.window_handles[-1])
        text2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/h2').text
        if '%s'%text1=='%s'%text2:
            # 关闭签到;取消关注
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/a[2]').click()
            finally:
                driver.find_element_by_xpath('/html/body/div[2]/div/a').click()
                driver.switch_to_window(driver.window_handles[0])
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[4]').click()
                text2=driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/h2/a').text
                if '%s'%text1!='%s'%text2:
                    # 关注板块
                    driver.switch_to_window(driver.window_handles[-1])
                    driver.find_element_by_xpath('/html/body/div[2]/div/a').click()
                    driver.switch_to_window(driver.window_handles[0])
                    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/span/a[4]').click()
                    text2 = driver.find_element_by_xpath('//*[@id="favorite-forums-grid"]/ul/li[1]/div[2]/h2/a').text
                    if '%s'%text1=='%s'%text2:
                        return 'true'
                    else:
                        driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                        return 'false3'
                else:
                    driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
                    return 'false2'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'fasle1'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def task(self):
        '''
        新手任务
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[6]/a').click()
        text1=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/span/a').text
        if '%s'%text1=='新手任务':
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return 'false'
    def wallet(self):
        '''
        钱包
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[7]/a').click()
        # 点击钱包进行判断
        text1=driver.find_element_by_xpath('/ html / body / div[4] / div[2] / div / div[1] / div[2] / div / div[1]').text
        # 操作文本
        text2=driver.find_element_by_xpath('//*[@id="credits_list_c0"]').text
    #     点击优惠券
        driver.find_element_by_xpath('//*[@id="record_tab"]/a[2]').click()
        text3=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/a[1]').text
        # 点击零钱记录
        driver.find_element_by_xpath('//*[@id="record_tab"]/a[3]').click()
        text4=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[3]/p').text
        # 点击我的佣金
        driver.find_element_by_xpath('//*[@id="myFriends"]').click()
        text5=driver.find_element_by_xpath('//*[@id="myfriends_list_c0"]').text
        # 点击订单中心
        driver.find_element_by_xpath('//*[@id="record_tab"]/a[5]').click()
        text6=driver.find_element_by_xpath('//*[@id="exchange_list_c0"]').text
        # 点击K币充值
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[2]/div/div[2]/a[1]').click()
        text7=driver.find_element_by_xpath('//*[@id="tabs-1"]/a').text
        # 点击兑换码兑换
        driver.find_element_by_xpath('//*[@id="tabs-2"]/a').click()
        text8=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/a').text
        # 点击充值记录
        driver.find_element_by_xpath('//*[@id="tabs-4"]/a').click()
        text9=driver.find_element_by_xpath('//*[@id="pay_list_c0"]').text
        # 点击零钱体现
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/a[2]').click()
        text10=driver.find_element_by_xpath('//*[@id="record_tab"]/a[1]').text
        # 点击零钱变更记录
        driver.find_element_by_xpath('//*[@id="record_tab"]/a[2]').click()
        text11=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/span').text
    # print('%s%s%s%s'%(text1[-1],text1[-2],text1[-3],text1[-4]))
    # print(text2)
    # print(text3)
    # print(text4[0:2])
    # print(text5)
    # print(text6)
    # print(text7)
    # print(text8)
    # print(text9)
    # print(text10)
    # print(text11[0:2])
        if '%s%s%s%s'%(text1[-4],text1[-3],text1[-2],text1[-1])=='我的钱包' and '%s'%text2=='操作' and '%s'%text3=='未使用' and '%s'%text4[0:2]=='零钱' and '%s'%text5=='昵称' and '%s'%text6=='商品名称' and '%s'%text7=='K币充值' and '%s'%text8=='充值' and '%s'%text9=='订单号' and '%s'%text10=='零钱提现' and '%s'%text11[0:2]=='客官':
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def Set_up1(self):
        '''
        设置：修改昵称
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        driver.find_element_by_xpath('//*[@id="name-edit"]').click()
        name1=time.strftime('%H%M%S',time.localtime(time.time()))
        driver.find_element_by_id('name').send_keys(name1)
        driver.find_element_by_id('nickname-save').click()
        time.sleep(3)
        try:
            driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        except:
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        name=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/span[1]/strong').text
        if '%s'%name=='%s'%name1:
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def Set_up2(self):
        '''
        设置：修改密码，邮箱，手机
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        driver.find_element_by_id('password-edit').click()
        # 修改密码
        text1=driver.find_element_by_xpath('//*[@id="h_title"]').text
        driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[1]/a').click()
        #修改邮箱
        driver.find_element_by_id('mail-revise').click()
        text2 =driver.find_element_by_id('h_title').text
        driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[1]/a').click()
        #修改手机
        driver .find_element_by_id('bind-tel').click()
        text3 = driver.find_element_by_id('h_title').text
        driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[1]/a').click()
        if '%s'%text1=='密码修改' and '%s'%text2=='邮箱修改' and '%s'%text3=='绑定手机号':
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def Set_up3(self):
        '''
        个人资料
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/span/a[2]').click()
        text1=time.strftime('%H%M%S',time.localtime(time.time()))
        driver.find_element_by_id('sign').clear()
        driver.find_element_by_id('sign').send_keys('快乐生活%s'%text1)
        driver.find_element_by_id('save-info').click()
        time.sleep(3)
        try:
            driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        except:
            time.sleep(3)
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        text2=driver.find_element_by_xpath('//*[@id="dou"]').text
        if '快乐生活%s'%text1=='%s'%text2:
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return 'false'
    def Set_up4(self):
        '''
        头像
        :return:
        '''
        # try:
        driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div[1]/a/span').click()
        driver.find_element_by_xpath('//*[@id="qd-nav"]/li[8]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/span/a[3]').click()
        text1=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[3]/form/a').text
        if '%s'%text1=='上传图片':
            return 'true'
        else:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
            return 'false'
        # except:
        #     driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (PersonalC().get_current_function_name()))
        #     return '代码有错'
    def close(self):
        driver.quit()
if __name__=='__main__':
    a=PersonalC()
    a.openC('http://www.kgc.cn/','502120020@qq.com','910227')
    print(a.course())




