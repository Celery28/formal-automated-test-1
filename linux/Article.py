# coding=utf-8
# 时间：
# 作者:
# 主要内容：文章
from selenium import webdriver
import time
import random
from pyvirtualdisplay import Display
display = Display(visible=0, size=(2880,1720))
display.start()
class Article(object):
    def openC(self, url, Account, Password):
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
    def details(self):
        '''
        文章详情页跳转正确
        :return:
        '''
        #文章总数
        zs=driver.find_elements_by_xpath('//*[@id="essay_box"]/div/div[1]/div/div')
        count=random.randint(1,len(zs))
        print(count)
        #文章题目
        text1=driver.find_element_by_xpath('//*[@id="essay_box"]/div/div[1]/div/div[%s]/div/div[1]/div[1]/a'%count).text

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="essay_box"]/div/div[1]/div/div[%s]/div/div[1]/div[1]/a'%count).click()
        driver.switch_to_window(driver.window_handles[-1])
        text2=driver.find_element_by_xpath('//*[@id="essay_box"]/div/div[1]/div/div[2]/div[1]/div/h6').text
        print(text1,text2)
        if text1==text2:
            return 'true'
        else:
            return 'fasle'
    def Fabulous(self):
        '''
        文章详情页点赞或取消点赞
        :return:
        '''
        # 文章总数
        zs = driver.find_elements_by_xpath('//*[@id="essay_box"]/div/div[1]/div/div')
        count = random.randint(1, 1)
        driver.find_element_by_xpath('//*[@id="essay_box"]/div/div[1]/div/div[%s]/div/div[3]/div/a' % count).click()
        driver.switch_to_window(driver.window_handles[-1])
        # class名
        time.sleep(1)
        text1=driver.find_element_by_id('article_zan').get_attribute('class')
        time.sleep(1)
        driver.find_element_by_id('article_zan').click()
        time.sleep(1)
        text2 = driver.find_element_by_id('article_zan').get_attribute('class')
        print(text1)
        print(text2)
        print(text1[-5:])
        print(text2[-5:])
        if text1[-5:]=='e_zan' and text2[-5:]=='yizan':
            return 'true'
        elif text1[-5:]=='yizan' and text2[-5:]=='e_zan':
            return 'true'
        elif text1[-5:]=='_zan ' and text2[-5:]=='yizan':
            return 'true'
        elif text1[-5:]=='yizan' and text2[-5:]=='_zan ':
            return 'true'
        else:
            return 'false'
    def close(self):
        driver.quit()
if __name__=='__main__':
    a=Article()
    a.openC('http://www.kgc.cn/article','502120020@qq.com','910227')
    print(a.Fabulous())