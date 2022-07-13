from models.web_hit import punch_the_clock


def main():
    try:
        url: str = 'https://test.com/'
        user: str = 'admin'
        password: str = 'admin'
        with open('logs.txt', 'a+') as logs:
            logs.write(punch_the_clock(url, user, password) + '\n')
    except Exception as error:
        print(error)


if '__main__' == __name__:
    main()
    exit(0)
