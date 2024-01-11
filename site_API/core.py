import pprint
from database.common.models import db, History
from typing import Any
from database.core import crud
from site_API.core import headers, params, site_api, url

db_write = crud.create()
db_read = crud.retrieve()

make_response = site_api.item_by_select_price()


def get_items_list(min_price: int, max_price: int, page: int) -> dict:
    """
    Функция делает запрос к api на основании указанных цен
    :param min_price: Минимальная цена
    :param max_price: Максимальная цена
    :param page: Номер страницы сайта с товарами
    :return: Словарь, ключом которого является цена, а значением список с названием,
             ссылкой на фото, ссылкой на страницу устройства.
    """
    items_data: dict = {}
    while True:
        response = make_response('GET', url, headers=headers, params=params,
                                 timeout=30, min_price=100, max_price=1500, page=1)
        pprint.pprint(response, indent=4)
        if response != 500:
            break
    response = response.json()

    for item in response['body']:
        price: float = float(item['prices']['salePrice']['formattedPrice'][4:])
        temp_dict = {price: {'price_str': item['prices']['salePrice']['formattedPrice'],
                             'item_name': item['title'],
                             'item_png': item['image']['imgUrl'],
                             'item_irl': item['link']}}
        items_data.update(temp_dict)

    pprint.pprint(items_data, indent=4)

    return items_data


def sort_by_low(items_data: dict) -> list:
    """
    Функция сортирует словарь на основе цены
    :param items_data: Словарь, ключ который является ценой устройства, а значение информация об этом устройстве
    :return: Лист с ключами, отсортированными по возрастанию.
    """
    key_list = [key for key in items_data.keys()]
    key_list.sort()

    return key_list


def sort_by_top(items_data: dict) -> list:
    """
    Функция сортирует словарь на основе цены
    :param items_data: Словарь, ключ который является ценой устройства, а значение информация об этом устройстве
    :return: Лист с ключами, отсортированными по убыванию.
    """
    key_list = [key for key in items_data.keys()]
    key_list.sort(reverse=True)

    return key_list


class CreateItemsInterface:
    @staticmethod
    def get_items_list():
        return get_items_list

    @staticmethod
    def get_keys_by_low():
        return sort_by_low

    @staticmethod
    def get_keys_by_top():
        return sort_by_top


if __name__ == '__main__':
    CreateItemsInterface()
