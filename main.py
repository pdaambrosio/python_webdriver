#!/home/kali-user/courses_projects/scripts/python_envs/web_hit_point/bin/python3
from models.web_hit import punch_the_clock
import pathlib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def main():
    """
    The main function attempts to punch the clock on a website using the provided URL, user, and
    password, and logs the result in an access.logs file. If an error occurs, it logs the error in an
    error.logs file.
    """
    try:
        url: str = 'https://url.com'
        user: str = os.getenv('WEB_USER')
        password: str = os.getenv('WEB_PASSWORD')
        with open(pathlib.Path().resolve()/'access.logs', 'a+') as access:
            access.write(punch_the_clock(url, user, password) + '\n')
    except Exception as err:
        with open(pathlib.Path().resolve()/'error.logs', 'a+') as error:
            error.write(f'{err}\n')


if '__main__' == __name__:
    main()
    exit(0)
