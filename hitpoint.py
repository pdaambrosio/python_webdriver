from time import sleep
from selenium import webdriver

PATH = '/home/kali-user/Downloads/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('url')
sleep(2)
driver.find_element_by_id('button-1020').click()
sleep(1)
driver.find_element_by_id('ext-135').send_keys('user')
driver.find_element_by_id('ext-137').send_keys('password')
sleep(1)
# driver.find_element_by_id('ext-139').click()
