import requests

import configuration
import data


def post_new_order(body):  # Функция создает новый заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
res = post_new_order(data.body_order)
print(res.json())

def get_order_by_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=track_order)
resp = get_order_by_track("111222")
print(resp.url)






