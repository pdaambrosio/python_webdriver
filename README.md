# python_webdriver

This is a simple example of how to use Selenium WebDriver with Python. It is based on the [Selenium Python Bindings](https://selenium-python.readthedocs.io/).

## Requirements

* Python 3.6+
* [Selenium Python Bindings](https://selenium-python.readthedocs.io/)
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

You need create a ".env" file with the following variables:

```bash
tee -a .env <<EOF
# .env
WEB_USERNAME=your_username
WEB_PASSWORD=your_password
EOF
```

Because the ".env" file contains sensitive information, it is ignored by Git.

In this project don't is necessary to download the ChromeDriver, because it is use the [webdriver-manager](https://pypi.org/project/webdriver-manager/) to download the ChromeDriver automatically.

But I recommend you use a virtual environment to install the dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For more information about virtual environments, see the [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/) article.

After that, you can run the script:

```bash
python3 main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
