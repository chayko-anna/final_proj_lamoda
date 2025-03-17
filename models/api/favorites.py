import requests

#due to authorisation problems is not used
class Favs:
    @staticmethod
    def add_to_favs_successful():
        data = {"sku":"RTLADN298701"}

        response = requests.post('https://www.lamoda.ru/api/v1/wishes/add', data=data)
        response_json = response.json()
        assert response.status_code == 200

    @staticmethod
    def add_to_favs_failed():
        data = {"sku":"RTLADN298701"}

        response = requests.post('https://www.lamoda.ru/api/v1/wishes/add', data=data)
        response_json = response.json()
        assert response.status_code == 200

    @staticmethod
    def remove_from_favs():
        data = {"sku":"RTLADN298701"}

        response = requests.post('https://www.lamoda.ru/api/v1/wishes/delete', data=data)
        response_json = response.json()
        assert response.status_code == 200