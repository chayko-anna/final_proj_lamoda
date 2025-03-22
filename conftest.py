import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
import os

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption('--browser_version')


@pytest.fixture(scope='function', autouse=True)
def browser_settings(request):
    browser.config.base_url = "https://lamoda.ru"
    browser.config.driver.maximize_window()
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION

    load_dotenv()

    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }
    options.capabilities.update(capabilities)

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
    yield browser

    browser.quit()
