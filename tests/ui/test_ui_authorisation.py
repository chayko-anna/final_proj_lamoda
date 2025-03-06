import allure
from models.ui.pages import LoginPage
from models.ui.pages import ProfilePage
from models.ui.pages import BasePage


@allure.tag('Browser')
@allure.epic('Authorisation')
@allure.testcase('Successful login')
def test_successful_authorisation(browser_settings):
    base = BasePage
    profile = ProfilePage
    login = LoginPage

    with allure.step('Open start page'):
        base.open()

    with allure.step('Click login button'):
        base.click_login_button()

    with allure.step('Fill in credentials'):
        login.fill_in_info()

    with allure.step('Click profile icon'):
        base.open_profile()

    with allure.step('Check profile info'):
        profile.verify_info()


@allure.testcase('Unsuccessful login')
def test_unsuccessful_authorisation(browser_settings):
    base = BasePage
    login = LoginPage

    with allure.step('Open start page'):
        base.open()

    with allure.step('Click login button'):
        base.click_login_button()

    with allure.step('Fill in wrong credentials'):
        login.fill_in_info()

    with allure.step('Click login button'):
        login.click_login_button()

    with allure.step('Check for unsuccessful login message'):
        login.unsuccessful_login_message_check()
