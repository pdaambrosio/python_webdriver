from time import sleep
from selenium import webdriver
from datetime import datetime

options: webdriver = webdriver.ChromeOptions()
options.headless = True

path: str = '/home/kali-user/Downloads/chromedriver'
driver: webdriver = webdriver.Chrome(path, options=options)

driver.get('URL')
sleep(2)
driver.find_element_by_id('button-1020').click()
sleep(1)
driver.find_element_by_id('ext-135').send_keys('USER')
driver.find_element_by_id('ext-137').send_keys('PASSWORD')
sleep(1)
driver.find_element_by_id('ext-139').click()
print(driver.find_element_by_id('ext-141').text, '-', datetime.now())
print(driver.title)
sleep(2)
driver.close()


