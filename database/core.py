from database.utils.CRUD import CRUDinterface
from database.common.models import db, History

db.connect()
db.create_tables([History])

crud = CRUDinterface()

if __name__=='__main__':
    crud()