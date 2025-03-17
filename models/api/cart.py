import requests
import json


class Cart:
    @staticmethod
    def add_to_cart_successful():
        data = json.dumps({"sku": "MP002XW0FXPSR3941"})
        headers = {
            "Content-Type": "application/json",
            'Cookie': 'lid=ZEACoWfWy/URPAl5IUEEAgA=; qrator_msid2=v2.0.1742136362.846.5f19c908fM2OC3Ks|rixnbLlw8gzhMUdh|/vchfj69Z/HXPf18iZkoEk5hvXakTAL/r22+wYoghHYPtSYb+2U/b0V00CxvvsIhW7f/xt6blBT89v90LATCFg==-kyNROd/jvERr8ExR1Nk0LiB99eU=; sid=NWFjZmMyZjNhODJiYmFkYzUzOTNhMzNlMzY4MTVlMTI=|1742128670|d9a4e19718c322491e6f2cc126de93c576ce6235; srv_menu_gender=women'
        }

        response = requests.post('https://www.lamoda.ru/api/v1/cart/add', data=data, headers=headers)
        assert response.status_code == 200

        response = requests.post('https://www.lamoda.ru/api/v1/cart/update', headers=headers,
                                 data=json.dumps({"items_included_in_order": ["MP002XW0FXPSR3638"]}))
        assert response.status_code == 200

        response = requests.get('https://www.lamoda.ru/api/v1/cart/get', headers=headers)
        assert "MP002XW0FXPSR3941" in response.text

    @staticmethod
    def add_to_cart_failed():
        data = json.dumps({"sku": "rtladn298701"})
        headers = {
            "Content-Type": "application/json",
            'Cookie': 'lid=ZEACoWfWy/URPAl5IUEEAgA=; qrator_msid2=v2.0.1742136362.846.5f19c908fM2OC3Ks|rixnbLlw8gzhMUdh|/vchfj69Z/HXPf18iZkoEk5hvXakTAL/r22+wYoghHYPtSYb+2U/b0V00CxvvsIhW7f/xt6blBT89v90LATCFg==-kyNROd/jvERr8ExR1Nk0LiB99eU=; sid=NWFjZmMyZjNhODJiYmFkYzUzOTNhMzNlMzY4MTVlMTI=|1742128670|d9a4e19718c322491e6f2cc126de93c576ce6235; srv_menu_gender=women'
        }

        response = requests.post('https://www.lamoda.ru/api/v1/cart/add', data=data, headers=headers)
        assert response.status_code == 400
        assert "No items on stock" in response.text

    @staticmethod
    def remove_from_cart():
        data = json.dumps({"sku":"MP002XW0FXPSR3638","geo":{"region_aoid":"7700000000000","city_aoid":"7700000000000"},"item_selection_enabled":"true"})
        headers = {
            "Content-Type": "application/json",
            'Cookie': 'lid=ZEACoGfW91RsQ09cMQ89AgA=; qrator_msid2=v2.0.1742194221.698.5f19c943dAj95NIQ|ihvpI4dXxzxViYhf|MBDeh0PMhCtVcO5jMrSzmFVBbuvM7sCQYG+oWdMGy8FLHNm3RKbvzwrIGWGofD4YaPj96msloD2jXV41oK1MhQ==-bFkFBpzqHDagbSqIqRmn8pNgc5A=; sid=ZGNiYjIwZjY5MDdlYjNkY2NlNjFiMDM0Mzc3ZDc2MTc=|1742140115|740a10e4848a8717ce0a01273bb6a8ae3cb60bab'
        }

        response = requests.post('https://www.lamoda.ru/api/v1/cart/add', headers=headers, data=data)
        assert response.status_code == 200

        data = json.dumps({"skus": ["MP002XW0FXPSR3638"]})
        response = requests.post('https://www.lamoda.ru/api/v1/cart/remove', data=data, headers=headers)
        assert response.status_code == 200

        response = requests.get('https://www.lamoda.ru/api/v1/cart/get', headers=headers)
        assert "MP002XW0FXPSR3638" not in response.text

