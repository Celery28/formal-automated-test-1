# coding=utf-8
# 时间：2017-07-06
# 作者:李伟
# 主要内容：就业实训
from selenium import webdriver
import time
import random
import inspect
from pyvirtualdisplay import Display
display = Display(visible=0, size=(2880,1720))
display.start()
class Training(object):
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
        try:
            global driver
            driver = webdriver.Chrome()
            driver.get(url)
            driver.implicitly_wait(30)
            driver.maximize_window()
            try:
                driver.find_element_by_link_text('登录').click()
            except:
                driver.refresh()
                driver.find_element_by_xpath('//*[@id="loginInfo"]/div/div/a[1]').click()
            driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys(Account)
            driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys(Password)
            driver.find_element_by_id('login').click()
            driver.implicitly_wait(30)
        except:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (Training().get_current_function_name()))
            return 'false'
    #     导航连链接禁用
    # def Navigation(self):
    #     '''
    #     就业实训基地页面导航栏跳转
    #     :return:
    #     '''
    #     try:
    #         driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[2]/a').click()
    #         driver.switch_to_window(driver.window_handles[-1])
    #         driver.refresh()
    #         if driver.title[:5]=='我的就业课':
    #             driver.switch_to_window(driver.window_handles[0])
    #             driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[3]/a').click()
    #             driver.switch_to_window(driver.window_handles[-1])
    #             driver.refresh()
    #             text=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/h3').text
    #             if text=='科技时尚':
    #                 driver.switch_to_window(driver.window_handles[0])
    #                 driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[4]/a').click()
    #                 driver.switch_to_window(driver.window_handles[-1])
    #                 driver.refresh()
    #                 text=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/h2').text
    #                 if text=='什么是前端?':
    #                     driver.switch_to_window(driver.window_handles[0])
    #                     driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[5]/a').click()
    #                     driver.switch_to_window(driver.window_handles[-1])
    #                     driver.refresh()
    #                     text=driver.find_element_by_xpath('/html/body/div[3]/div[1]/h3').text
    #                     if text=='不是所有Linux培训都叫云计算':
    #                         driver.switch_to_window(driver.window_handles[0])
    #                         driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[6]/a').click()
    #                         driver.switch_to_window(driver.window_handles[-1])
    #                         driver.refresh()
    #                         text=driver.title[:3]
    #                         if text=='大数据':
    #                             driver.switch_to_window(driver.window_handles[0])
    #                             driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[7]/a').click()
    #                             driver.switch_to_window(driver.window_handles[-1])
    #                             driver.refresh()
    #                             text=driver.find_element_by_xpath('//*[@id="__01"]/table/tbody/tr[1]/td/div[2]/div/div[1]/div[1]').text
    #                             if text=='营销新动力 从这里起航':
    #                                 driver.switch_to_window(driver.window_handles[0])
    #                                 driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[8]/a').click()
    #                                 driver.switch_to_window(driver.window_handles[-1])
    #                                 driver.refresh()
    #                                 if driver.title[:6]=='线下服务中心':
    #                                     driver.switch_to_window(driver.window_handles[0])
    #                                     driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[9]/a').click()
    #                                     driver.switch_to_window(driver.window_handles[-1])
    #                                     driver.refresh()
    #                                     if driver.title[:4]=='商品兑换':
    #                                         driver.switch_to_window(driver.window_handles[0])
    #                                         driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[10]/a').click()
    #                                         driver.switch_to_window(driver.window_handles[-1])
    #                                         driver.refresh()
    #                                         text=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/h2/span[6]/a').text
    #                                         if text=='全部版块':
    #                                             driver.switch_to_window(driver.window_handles[0])
    #                                             driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[11]/a').click()
    #                                             if driver.title[:4]=='证书学籍':
    #                                                 return 'true'
    #                                             else:
    #                                                 driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                                                 return 'false'
    #                                     else:
    #                                         driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                                         return 'false'
    #                                 else:
    #                                     driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                                     return 'false'
    #                             else:
    #                                 driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                                 return 'false'
    #                         else:
    #                             driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                             return 'false'
    #                     else:
    #                         driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                         return 'false'
    #                 else:
    #                     driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                     return 'false'
    #             else:
    #                 driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #                 return 'false'
    #         else:
    #             driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #             return 'false'
    #     except:
    #         driver.save_screenshot("test_%s.png" % (Training().get_current_function_name()))
    #         return 'false'
    def look(self):
        '''
        看课
        :return:
        '''
        # 获取分类总数
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul[2]/li/a/img').click()
            driver.switch_to_window(driver.window_handles[-1])
            count = driver.find_elements_by_xpath('/html/body/div[4]/div/div')
            print(len(count))
            count1 = random.randint(1, len(count))
            # 选取免费课程
            count2 = random.randint(1, 3)
            print(count1, count2)
            js = "var q=document.documentElement.scrollTop=600"
            driver.execute_script(js)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[%s]/ul/li[%s]/div[1]/h3/a' % (count1, count2)).click()
            driver.find_element_by_xpath('//*[@id="player-content"]/div/div[4]/a').click()
            time.sleep(2)
            js = "var q=document.documentElement.scrollTop=500"
            driver.execute_script(js)
            # driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/h2/a').click()
            count3 = random.randint(4, 5)
            print(count3)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[%s]/div[1]/h3/a' % count3).click()
            return 'true'
        except:
            driver.save_screenshot("./report/screen_shot/failed/test_%s.png" % (Training().get_current_function_name()))
            return 'false'
    def close(self):
        driver.quit()
if __name__=='__main__':
    a=Training()
    a.openC('http://a.kgc.cn/','502120020@qq.com','123456')
    print(a.look())