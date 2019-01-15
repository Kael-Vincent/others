#coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
desired_caps={
    'platformName':'Android',
    'platformVersion':'6.0.1',
    'deviceName':'b298daa7',
    'automationName':'Appium',
    # 'app':'D:/Users/yangyongqing/Documents/WXWork/1688850068366400/Cache/File/2017-09/yihui_inner_net_test.apk',
    'appPackage':'com.dafy.onecollection',
    'appActivity':'com.dafy.onecollection.activity.MainActivity'
        }

# def sign():

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# TouchAction(driver).press(x=520, y=1900).release().perform()
# sleep(1)
# driver.save_screenshot(r'打卡截图.png')

# if driver.find_element_by_id('com.dafy.onecollection:id/phone_et'):
#     driver.find_element_by_id('com.dafy.onecollection:id/phone_et').clear()
#     driver.find_element_by_name(u'手机号码').send_keys('13076960169')
#     driver.find_element_by_name(u'短信验证码').clear()
#     driver.find_element_by_name(u'短信验证码').send_keys('123456')
#     driver.find_element_by_id(u'登 录').click()
# elif driver.find_element_by_id('com.dafy.onecollection:id/gab_order_success_dialog'):
#     driver.find_element_by_id('com.dafy.onecollection:id/confirm_btn').click()
#     driver.find_element_by_id('com.dafy.onecollection:id/confirm_btn').click()
# else:
#     driver.find_element_by_class_name('android.widget.FrameLayout')
#
#
# driver.find_element_by_id('tab_my_iv').click()
try:
    driver.find_element_by_id('com.dafy.onecollection:id/tab_my_iv').click()
    driver.find_element_by_id('com.dafy.onecollection:id/tab_my_tv').click()
except Exception as e:
    print(e)



