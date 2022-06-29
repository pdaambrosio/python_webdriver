from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PATH = '/home/kali-user/Downloads/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com/')
driver.find_element_by_class_name('gNO89b').submit()
