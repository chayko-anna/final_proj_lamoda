import requests
import logging
from models.api.cookies import CookieManager
from utils.config_web import headers, url_api, params

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Cart:
    def checking_products_cart(self):
        cart_url = f'{url_api}/cart/v2/items'
        response_cart = requests.get(cart_url,
                                     params=params,
                                     headers=headers,
                                     cookies=CookieManager.get_browser_cookies(),
                                     )
        response_json_cart = response_cart.json()
        logging.info(response_json_cart['state']['title'])
        logging.info(response_json_cart['data']['totals'])

        return response_json_cart['data']['totals']['items_count']