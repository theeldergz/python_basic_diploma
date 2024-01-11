from database.common.models import db, History
from database.core import crud
from site_API.core import CreateItemsInterface


core_api = CreateItemsInterface()

db_write = crud.create()
db_read = crud.retrieve()

create_items_list = core_api.get_items()
phones: dict = create_items_list(min_price=100, max_price=800, page=1)

for key in phones.keys():

    history_data = [{'price': phones[key].get('price_str'),
                     'item_url': phones[key].get('item_url'),
                     'item_name': phones[key].get('item_name')}]

    db_write(db, History, history_data)

retrieved = db_read(db, History, History.price, History.item_url, History.item_name)

for element in retrieved:
    print(element.price, element.item_url, element.item_name)
