from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import Any


def punch_the_clock(url: str, user: str, password: str) -> str:
    page_result: Any

    options: webdriver = webdriver.ChromeOptions()
    options.headless = True
    path: str = 'chromedriver'
    driver: webdriver = webdriver.Chrome(path, options=options)
    # driver: webdriver = webdriver.Chrome(path, options=None)

    driver.get(url)
    sleep(3)
    driver.find_element(By.ID, 'button-1020').click()
    sleep(1)
    driver.find_element(By.ID, 'ext-135').send_keys(user)
    driver.find_element(By.ID, 'ext-137').send_keys(password)
    sleep(1)
    driver.find_element(By.ID, 'ext-139').click()
    sleep(1)
    page_result = driver.find_element(By.ID, 'ext-141').text
    date: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sleep(2)
    driver.close()
    return f'{page_result} - {date}'
