from typing import Dict, List, TypeVar
from peewee import ModelSelect
from database.common.models import db, ModelBase

T = TypeVar('T')


def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)

    return response


class CRUDinterface():
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == '__main__':
    CRUDinterface()
