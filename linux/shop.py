# coding=utf-8
# 时间：2017-07-05
# 作者:李伟
# 主要内容：商城购买
from selenium import webdriver
import time
import random
import inspect
from pyvirtualdisplay import Display
display = Display(visible=0, size=(2880,1720))
display.start()
from selenium import webdriver
import time
import random
import inspect
class shop(object):

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
            driver.maximize_window()
            driver.find_element_by_link_text('登录').click()
            driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys(Account)
            driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys(Password)
            driver.find_element_by_id('login').click()
            driver.implicitly_wait(30)
        except:
            driver.save_screenshot("test_%s.png" % (shop().get_current_function_name()))
            return 'false'
    def Buy(self):
        '''
        购买商品
        :return:
        '''
        try:
            # 总个数
            count=driver.find_elements_by_xpath('//*[@id="yw2"]/ul/li')
            print(len(count))
            # 假数
            a=1
            while a>0:
                count1=random.randint(1,len(count))
                driver.find_element_by_xpath('//*[@id="yw2"]/ul/li[%s]/h2/p/a'%count1).click()
                # 计算类别
                count=driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div')
                if len(count)==2:
                    count2=int(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/span[2]').text)
                    if count2>0:
                        break
                    else:
                        driver.back()
                        continue
                elif len(count)==3:
                    count2=int(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[3]/span[2]').text)
                    if count2>0:
                        break
                    else:
                        driver.back()
                        continue
                elif len(count) == 3:
                    count2 = int(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[4]/span[2]').text)
                    if count2 > 0:
                        break
                    else:
                        driver.back()
                        continue
            if len(count) == 2:
                # 获取库存总数
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/input').clear()
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys(count2+1)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[3]/a').click()
                text=driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[2]').text
                if text[0:6]=='您的兑换数量':
                    driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[1]/a').click()
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/input').clear()
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys(1)
                    text1=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[1]/span[1]/em').text
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[3]/a').click()
                else:
                    return 'false'
            elif len(count) == 3:
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[3]/div/input').clear()
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[3]/div/input').send_keys(count2 + 1)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[4]/a').click()
                text = driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[2]').text
                if text[0:6] == '您的兑换数量':
                    driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[1]/a').click()
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[3]/div/input').clear()
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[3]/div/input').send_keys(1)
                    text1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[1]/span[1]/em').text
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[4]/a').click()
                else:
                    return 'false'
            elif len(count) == 3:
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[4]/div/input').clear()
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[4]/div/input').send_keys(count2 + 1)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[5]/a').click()
                text = driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[2]').text
                if text[0:6] == '您的兑换数量':
                    driver.find_element_by_xpath('//*[@id="dialog0"]/div[2]/div[1]/a').click()
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[4]/div/input').clear()
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[4]/div/input').send_keys(1)
                    text1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[1]/span[1]/em').text
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/p[5]/a').click()
                else:
                    return 'false'
                # 商品剩余总数
            driver.find_element_by_id('name').clear()
            driver.find_element_by_id('name').send_keys('测试')
            driver.find_element_by_id('country').click()
            # 下拉框没有随机，原因每个省市下属区县不同，冒烟没必要
            driver.find_element_by_xpath('//*[@id="country"]/option[2]').click()
            driver.find_element_by_id('city').click()
            driver.find_element_by_xpath('//*[@id="city"]/option[2]').click()
            driver.find_element_by_id('address').clear()
            driver.find_element_by_id('address').send_keys('测试测试测试')
            driver.find_element_by_id('code').clear()
            driver.find_element_by_id('code').send_keys('100090')
            driver.find_element_by_id('telphone').clear()
            driver.find_element_by_id('telphone').send_keys('13581917640')
            driver.find_element_by_xpath('//*[@id="good"]/div[2]/div[2]/div/form/div[6]/div/textarea').send_keys('测试数据')
            driver.find_element_by_xpath('//*[@id="good"]/div[2]/div[2]/div/form/div[7]/a[1]').click()
            driver.switch_to_window(driver.window_handles[-1])
            text2=driver.find_element_by_xpath('//*[@id="J_basePriceArea"]/strong').text
            if text2==text1[1:]:
                return 'true'
            else:
                driver.save_screenshot("test_%s.png" % (shop().get_current_function_name()))
                return 'false1'
        except:
            driver.save_screenshot("test_%s.png" % (shop().get_current_function_name()))
            return 'false'
    def close(self):
        driver.quit()

if __name__=='__main__':
    a=shop()
    a.openC('http://www.kgc.cn/goods','502120020@qq.com','910227')
    print(a.Buy())