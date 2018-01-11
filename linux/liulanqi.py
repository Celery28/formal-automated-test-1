# coding=utf-8
# 时间：
# 作者:
# 主要内容：
from selenium import webdriver
import time
from pyvirtualdisplay import Display
display = Display(visible=0, size=(2880,1720))
display.start()
driver=webdriver.Chrome()
driver.get('http://www.kgc.cn/teacher/117.shtml')
driver.maximize_window()
time.sleep(3)
driver.save_screenshot('2.png')
driver.find_element_by_link_text('登录').click()
driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys('502120020@qq.com')
driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys('910227')
driver.find_element_by_id('login').click()
time.sleep(3)
#driver.maximize_window()
driver.save_screenshot('1.png')
