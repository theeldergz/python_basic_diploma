import peewee as pw
from datetime import datetime

db = pw.SqliteDatabase('lecture.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    price = pw.TextField()
    min_price = pw.TextField()
    max_price = pw.TextField()
    item_url = pw.TextField()
    item_name = pw.TextField()

