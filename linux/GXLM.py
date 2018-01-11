# coding=utf-8
# 时间：
# 作者:
# 主要内容：
from selenium import webdriver
import inspect
import time
import random
from pyvirtualdisplay import Display
display = Display(visible=0, size=(2880,1720))
display.start()
class gxlm(object):
    def get_current_function_name(self):
        '''
        返回当前方法名
        :return:
        '''
        return inspect.stack()[1][3]
    def openC(self,url,Account,Password):
        global driver
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys(Account)
        driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys(Password)
        driver.find_element_by_id('login').click()
        driver.implicitly_wait(30)
    def ygxlm(self):
        '''
        院校学员进入其他高校出现提示语，有为true,无为false
        :return
        '''
        driver.find_element_by_id('expandSchoolFriendLink').click()
        time.sleep(2)
        count=driver.find_elements_by_xpath('//*[@id="index-yx"]/li')
        count1=random.randint(2,len(count))
        driver.find_element_by_xpath('//*[@id="index-yx"]/li[%s]'%count1).click()
        driver.switch_to_window(driver.window_handles[-1])
        text=driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/p').text
        if text=='您已绑定北京大学院校，去那看看吧':
            return 'true'
        else:
            return 'false'
    def ngxlm(self):
        '''
        非高校学院进入高校出现提示框，有为true,无为false
        :return:
        '''
        driver.find_element_by_id('expandSchoolFriendLink').click()
        time.sleep(2)
        count = driver.find_elements_by_xpath('//*[@id="index-yx"]/li')
        count1 = random.randint(1, len(count))
        driver.find_element_by_xpath('//*[@id="index-yx"]/li[%s]' % count1).click()
        driver.switch_to_window(driver.window_handles[-1])
        text = driver.find_element_by_xpath('/html/body/div[5]/div[1]/span').text
        if text=='请输入您的相关信息以供审核':
            return 'true'
        else:
            return 'false'
    def kcmc(self):
        '''
        高校学院进度本高校，点击课程进入验证课程名称，对为true,错为false
        :return:
        '''
        driver.find_element_by_xpath('//*[@id="index-yx"]/li[1]/a/img').click()
        driver.switch_to_window(driver.window_handles[-1])
        text=driver.find_element_by_xpath('/html/body/div[4]/div/ul[1]/li[1]/a/img').get_attribute('alt')
        driver.find_element_by_xpath('/html/body/div[4]/div/ul[1]/li[1]/a/img').click()
        text1=driver.find_element_by_xpath('//*[@id="title"]/h2').text
        if text==text1:
            return 'true'
        else:
            return 'false'
    def close(self):
        driver.quit()
if __name__=='__main__':
    a=gxlm()
    a.openC('http://www.kgc.cn/','15701572966','Csz123456')
    print(a.kcmc())