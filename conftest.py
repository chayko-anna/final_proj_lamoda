import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.page_load_strategy = 'eager'
    browser.config.base_url = 'https://www.lamoda.ru/'
    browser.driver.maximize_window()

    yield

    browser.quit()
