import requests
import configuration
import data


def post_new_order(body):  # Функция создает новый заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)





def get_order_by_track(track): # Функция на запрос заказа по номеру
        return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=track)






