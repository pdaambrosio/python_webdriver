def punch_the_clock(url: str, user: str, password: str) -> str:
    from time import sleep
    from selenium import webdriver
    from datetime import datetime
    from typing import Any

    page_title: str
    page_result: Any

    options: webdriver = webdriver.ChromeOptions()
    options.headless = True
    path: str = './chromedriver'
    driver: webdriver = webdriver.Chrome(path, options=options)

    driver.get(url)
    sleep(2)
    driver.find_element_by_id('button-1020').click()
    sleep(1)
    driver.find_element_by_id('ext-135').send_keys(user)
    driver.find_element_by_id('ext-137').send_keys(password)
    sleep(1)
    driver.find_element_by_id('ext-139').click()
    page_title = driver.title
    page_result = driver.find_element_by_id('ext-141').text
    date: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sleep(2)
    driver.close()
    return f'{page_title}\n{page_result} - {date}'


def main():
    try:
        url: str = 'https://www.hitpoint.co.jp/'
        user: str = 'admin'
        password: str = 'admin'
        with open('logs.txt', 'w') as logs:
            logs.write(punch_the_clock(url, user, password))
    except KeyboardInterrupt:
        print('\nBye!')


if '__main__' == __name__:
    main()
    exit(0)
