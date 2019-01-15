from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = 'http://www.yihuivip.cn:82/#/login'

driver.get(url=url)
sleep(3)
# driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div/input').send_keys('13200000000')
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('123123')
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()




