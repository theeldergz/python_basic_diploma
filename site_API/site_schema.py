from settings import SiteSettings
from site_API.utils.site_api_hadler import SiteApiInterface


site = SiteSettings()

url = "https://" + site.host_api

params = {
    'search': 'phones',
    'categoryID': '5090301',
    'minPrice': '100',
    'maxPrice': '1000',
    'shipFromCountry': 'RU',
    'freeShipping': '1',
    'fourStarsAndUp': '1',
    'sort': 'orders',
    'page': '1',
}

headers = {
    'Authorization': f'Bearer {site.api_key.get_secret_value()}'
}

site_api = SiteApiInterface()

if __name__ == "__main__":
    site_api()

