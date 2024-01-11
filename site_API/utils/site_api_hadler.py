from typing import Dict

import requests


def _make_response(method: str, url: str, headers: Dict, params: Dict,
                   timeout: int, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def item_by_select_price(method: str, url: str, headers: Dict, params: Dict,
                         timeout: int, min_price=100, max_price=100000, page=1, func=_make_response):
    print(params)

    params['minPrice'], params['maxPrice'], params['page'] = str(min_price), str(max_price), str(page)
    params['sort'] = 'price_asc'
    print(params)
    response = func(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    return response


class SiteApiInterface:
    @staticmethod
    def _make_response():
        return _make_response

    @staticmethod
    def item_by_select_price():
        return item_by_select_price


if __name__ == '__main__':
    SiteApiInterface()
