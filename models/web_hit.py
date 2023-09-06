from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from typing import Any


def punch_the_clock(url: str, user: str, password: str) -> str:
    """
    The function `punch_the_clock` logs into a website using the provided URL, username, and password,
    performs some actions, retrieves a page result, and returns the result along with the current date
    and time.
    
    :param url: The `url` parameter is a string that represents the URL of the webpage where the clock
    punching functionality is located
    :type url: str
    :param user: The `user` parameter is a string that represents the username or user ID used to log in
    to the website or application
    :type user: str
    :param password: The `password` parameter is a string that represents the password for the user to
    log in to the website specified by the `url` parameter
    :type password: str
    :return: a string that consists of the page result and the current date and time.
    """
    page_result: Any

    options: webdriver = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service_path: Service = Service(ChromeDriverManager().install())
    driver: webdriver = webdriver.Chrome(service=service_path, options=options)
    
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
    date: str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    sleep(2)
    driver.close()
    return f'{page_result} - {date}'
