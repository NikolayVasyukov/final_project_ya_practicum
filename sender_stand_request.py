import requests

import configuration
import data


def post_new_order(body):  # Функция создает новый заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
res = post_new_order(data.body_order)
print(res.json())






