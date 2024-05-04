from typing import Dict

from datastore.mongodb import MongoDBConnection
from entities.schemas import ItemCreate, ItemGet, ItemPut, ItemDelete


class HandlerRequest:
    def __init__(self, settings):
        self.settings = settings
        self.conn = MongoDBConnection(self.settings.HOST, self.settings.TODOS_DBNAME)

    def create_new_item(self, item: ItemCreate) -> Dict[str, str]:
        try:
            res = self.conn.insert_new_todoItem(item)
            return res
        except Exception as e:
            raise e

    def get_item(self, item: ItemGet) -> Dict[str, str]:
        try:
            res = self.conn.get_todoItem(item)
            return res
        except Exception as e:
            raise e

    def update_item(self, item: ItemPut) -> Dict[str, str]:
        try:
            res = self.conn.update_todoItem(item)
            return res
        except Exception as e:
            raise e

    def delete_item(self, item: ItemDelete) -> Dict[str, str]:
        try:
            res = self.conn.delete_todoItem(item)
            return res
        except Exception as e:
            raise e