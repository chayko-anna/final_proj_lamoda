import json
import logging

import allure
import jsonschema
import pytest
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from requests import Response

from utils import load_schema


url = "https://www.lamoda.ru/"
login = "example1200@example.com"
pwd = "123456"


def test_successful_auth():
    with allure.step("Successful API authorisation"):
        res = requests.post(url=url + "login",
                            data={"Email": login,
                                  "Password": pwd,
                                  "Remember me": False},
                            allow_redirects=False)
        allure.attach(body=res.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=res.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(res.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with allure.step("Get cookie from API"):
        cookie = res.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step("Set cookie from API"):
        browser.open(url)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(url)
        browser.driver.delete_all_cookies()


@pytest.mark.parametrize('settings_browser', [(login, pwd), (login, pwd)], indirect=True)
def test_unsuccessful_auth():
    with allure.step("API authorisation with wrong password"):
        res = requests.post(url=url + "login",
                            data={"Email": login,
                                  "Password": pwd,
                                  "Remember me": False},
                            allow_redirects=False)
        allure.attach(body=res.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=res.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(res.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with allure.step("Get cookie from API"):
        cookie = res.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step("Set cookie from API"):
        browser.open(url)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(url)
        browser.driver.delete_all_cookies()
