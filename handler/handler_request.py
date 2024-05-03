from typing import Dict

from datastore.mongodb import MongoDBConnection
from entities.schemas import MyHandlerEnvVars,Item,ToDoItem

class HandlerRequest:

    def __init__(self, settings):
        self.settings = settings
        self.MongoDBConnection = MongoDBConnection(self.settings.HOST, self.settings.TODOS_DBNAME)

    def create_new_item(self, item: Item) -> Dict[str, str]:
        with self.MongoDBConnection as conn:
            res = conn.insert_new_todoItem(item)

        return res

