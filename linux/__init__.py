# coding=utf-8
# 时间：
# 作者:
# 主要内容：
# from selenium import webdriver
# import random
#
# import time
# driver=webdriver.Chrome()
# driver.get('http://www.kgc.cn/bbs/post/146939.shtml')
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys('13263186099')
# driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys('123456')
# driver.find_element_by_id('login').click()
# driver.implicitly_wait(30)
# a1 = driver.find_elements_by_xpath('//*[@id="yw0"]/ul/li')
# b1 = random.randint(1,len(a1))
# driver.find_element_by_xpath('//*[@id="level%s"]/div[2]/div[4]/p/a[1]'%b1).click()

# a='12412312'
# print(a[2:4])
# driver = webdriver.Chrome()
# driver.get('http://www.kgc.cn/')
# driver.maximize_window()
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys('502120020@qq.com')
# driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys('654321')
# driver.find_element_by_id('login').click()
# driver.implicitly_wait(30)
# driver.find_element_by_link_text('python...').click()
# driver.find_element_by_xpath('//*[@id="qd-nav"]/li[2]/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div[2]/div[2]/a').click()
# time.sleep(3)
# print(driver.find_element_by_xpath('//*[@id="player-right"]/div/div[1]/h1').text)
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.set_window_size(1055, 800)
# browser.get("http://www.baidu.com/")
# # browser.find_element_by_id("idClose").click()
# time.sleep(5)
#
# browser.save_screenshot("shot.png")
# browser.quit()
#
# import inspect
#
#
# def get_current_function_name():
#     return inspect.stack()[1][3]
#
#
# class MyClass:
#     def c(self):
#         print("%s" % (get_current_function_name()))
#
#
# if __name__ == "__main__":
#     myclass = MyClass()
#     myclass.c()

