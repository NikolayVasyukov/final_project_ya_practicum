import requests
import configuration
import data


def post_new_order(body):  # Функция создает новый заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)



def get_new_order(): # Функция сохраняет номер трека
    order_body = data.body_order.copy()
    response = post_new_order(order_body)
    track = response.json()["track"]
    return track


def get_order_by_track(new_track=get_new_order()): # Функция на запрос заказа по номеру
    track = {'t': new_track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=track)






