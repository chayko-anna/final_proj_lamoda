from selene import browser, have, by
from dotenv import load_dotenv
import os
import time


class LoginPage:
    @staticmethod
    def fill_in_info():
        load_dotenv()
        login = os.getenv('LOGIN')
        pwd = os.getenv('PASSWORD')

        browser.element('[class="input-material__input-user-agent input-material__input"]').click().type(login)
        browser.element('[aria-label="Войти"]').click()
        browser.element('[name="password"]').click().type(pwd)
        browser.element('[aria-label="Войти"]').click()
        time.sleep(1)

    @staticmethod
    def click_login_button():
        browser.element('[class="x-button x-button_primaryFilledWeb7184 x-button_56 _submit_q2ixp_38 ui-submit_button"]').click()

    @staticmethod
    def unsuccessful_login_message_check():
        browser.should(have.text('Неверный логин или пароль.'))


class BasePage:
    @staticmethod
    def open():
        browser.open('/')

    @staticmethod
    def open_item_page(item_link):
        browser.open(item_link)

    @staticmethod
    def select_size():
        browser.element('[class="_sizeValue_14ecl_285"]').click()
        browser.element(by.text('36/38 RUS')).click()

    @staticmethod
    def click_login_button():
        browser.element('[class="x-button x-button_secondaryFilledWeb7184 x-button_32 _button_hqrm4_8 _item_hqrm4_13"]').click()

    @staticmethod
    def open_profile():
        browser.element('[class="_text_jdmgo_41"]').click()

    @staticmethod
    def check_availability():
        browser.element('[class="x-button x-button_secondaryPremium x-button_48 _cartButton_1gbkc_11"]').should(have.text('Товаров нет в наличии'))


class ProfilePage:
    @staticmethod
    def open():
        browser.open('/customer/account/')

    @staticmethod
    def verify_info():
        browser.element('[class="_text_jdmgo_41"]').should(have.text('Профиль'))
