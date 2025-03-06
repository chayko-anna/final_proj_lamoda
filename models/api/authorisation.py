import logging
import requests
from utils.config_web import headers, json_data, url_api
from models.api.cookies import CookieManager


class Authorisation:
    def __init__(self):
        self.cookie_manager = CookieManager()

    def send_request(self, url):
        response = requests.post(
            url,
            headers=headers,
            json=json_data,
            cookies=self.cookie_manager.get_browser_cookies(),
            allow_redirects=False
        )
        return response

    def login(self):
        response = self.send_request(f'{url_api}/user/v1.1/login')
        response_json = response.json()

        assert response.status_code == 200, logging.info(response_json['state']['title'])
        logging.info(response_json['state']['title'])

    def logout(self):
        response = self.send_request(f'{url_api}/user/v1.1/logout')
        response_json = response.json()

        assert response.status_code == 200, logging.info(response_json['state']['title'])
        logging.info(response_json['state']['title'])