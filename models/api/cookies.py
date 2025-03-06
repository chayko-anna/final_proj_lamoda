from selene import browser


class CookieManager:
    @staticmethod
    def get_browser_cookies():
        selenium_cookies = browser.driver.get_cookies()
        return {cookie['name']: cookie['value'] for cookie in selenium_cookies}