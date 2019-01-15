from selenium import webdriver
from time import sleep


def web():
    url = 'http://collection.admin.test.com/#/login'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    # try:
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div[1]/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div[1]/input').send_keys('13300000000')
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div/li[1]/div').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div/li[1]/ul/a[1]/li').click()
    driver.find_element_by_xpath('//*[@id="pane-first"]/div/form[1]/div[1]/div/div/input').send_keys('abcde')
    driver.find_element_by_xpath('//*[@id="pane-first"]/div/form[1]/div[2]/div/div/div/input').send_keys('qwer')
    driver.find_element_by_xpath('//*[@id="pane-first"]/div/form[1]/div[3]/div/div/input').send_keys('huannhahg')
    driver.find_element_by_xpath('//*[@id="pane-first"]/div/form[1]/div[4]/div/div/input').send_keys('iiouyiyhoh')
    # sleep(10)
    driver.find_element_by_xpath('//*[@id="tab-second"]').click()
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/form/div[1]/div/div/input').send_keys('hhoahg')
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/form/div[2]/div/div/div/input').send_keys('sejkkjhkakbg')
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/form/div[3]/div/div/input').send_keys('jkangkkhakg')
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/form/div[4]/div/div/input').send_keys('hioohalhlg')
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/form/div[5]/div/div/input').send_keys('uhhakljkhkjhkgha')
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[1]/label[1]/span[1]/span').click()
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/span[2]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/span[2]/div/div/input').send_keys(30)
    driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[2]/div/button/span').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div/li[1]/ul/a[2]/li').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[1]/div[1]/div/div/div/input').send_keys('johohhhih')
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[2]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[1]/div/button[2]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[1]/div/button[3]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[1]/div/button[4]').click()
    sleep(10)

    driver.quit()
    # driver.close()
    # except Exception as e:
    #     driver.close()
    #     print(e)


if __name__ == '__main__':
    web()
