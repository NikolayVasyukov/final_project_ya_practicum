import requests

import configuration
import data


def post_new_order(body):  # Функция создает новый заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

res = post_new_order(data.body_order)
print(res.json())

def get_new_order(): # Функция сохраняет номер трека
    order_body = data.body_order.copy()
    response = post_new_order(order_body)
    track = response.json()["track"]
    return track
print(get_new_order())

def get_order_by_track(new_track): # Функция на запрос заказа по номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=new_track)
resp = get_order_by_track("t=" + "670503")
print(resp.url)

assert resp.status_code == 200





