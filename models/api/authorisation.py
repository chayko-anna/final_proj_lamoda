import requests


class Authorisation:

    @staticmethod
    def login(login, password):
        data = {"login": login, "password": password}
        response = requests.post('https://www.lamoda.ru/api/v1/customer/login', data=data)

        assert response.status_code == 200

        response = requests.post('https://sentry-js.lamoda.ru/api/2/store/?sentry_key=8ddb7c59cddd4becb87a4b92279a26ab&sentry_version=7')

        assert response.status_code == 200

    @staticmethod
    def logout():
        response = requests.post('https://www.lamoda.ru/customer/account/logout/')

        assert response.status_code == 200

