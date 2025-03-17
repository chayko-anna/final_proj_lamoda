import allure
from models.api.authorisation import Authorisation
from dotenv import load_dotenv
import os


@allure.epic('Authorisation')
@allure.testcase('Successful login')
def test_successful_auth():
    auth = Authorisation()
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    with allure.step("Successful API authorisation"):
        auth.login(login, password)


@allure.testcase('Unsuccessful login')
def test_unsuccessful_auth():
    auth = Authorisation()
    load_dotenv()
    login = 'sdfdfsdfsdf@dfg.com'
    password = 'eewrwerwerwer'
    with allure.step("API authorisation with wrong password"):
        auth.login(login, password)
