from typing import Dict

from entities.schemas import MyHandlerEnvVars, ToDoItem
import json
from mongoengine import connect
from entities.schemas import Item
class MongoDBConnection(object):
    """MongoDB Connection"""
    def __init__(self, host: str, db_name: str):
        self.host = host
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = connect(f'{self.db_name}', host=self.host)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def insert_new_todoItem(self, item: Item) -> Dict[str,str]:

        todo_item = ToDoItem(title=item.title, description=item.description)
        try:
            todo_item.save()
        except Exception as e:
            raise e
        res = {"id": todo_item.item_id, "title": todo_item.title, "description": todo_item.description,
               "status": todo_item.status}
        return res
