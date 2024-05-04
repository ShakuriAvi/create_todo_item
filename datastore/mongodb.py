from typing import Dict
import logging

from entities.schemas import ToDoItem, ItemCreate, ItemGet, ItemPut, ItemDelete
from mongoengine import connect

class MongoDBConnection(object):
    """MongoDB Connection"""
    def __init__(self, host: str, db_name: str):
        self.host = host
        self.db_name = db_name
        self.connection = connect(self.db_name, host=self.host)


    def insert_new_todoItem(self, item: ItemCreate) -> Dict[str,str]:
        todo_item = ToDoItem(title=item.title, description=item.description)
        try:
            todo_item.save()
            res = {"id": str(todo_item.item_id), "title": todo_item.title, "description": todo_item.description,
                   "status": todo_item.status}
            logging.info(f"Results from DB insert: {res}")
            return res
        except Exception as e:
            logging.error(f"Error saving todo item: {e}")
            raise e

    def get_todoItem(self, item: ItemGet) -> Dict[str,str]:
        try:
            todo_item = ToDoItem.objects.get(item_id=item.id)
            logging.info(f"Results from DB insert: {todo_item}")
            res = self.__make_todo_response(todo_item)
            return res
        except Exception as e:
            logging.error(f"Error todo item: {e}")
            raise e

    def update_todoItem(self, item: ItemPut) -> Dict[str,str]:
        try:
            todo_item = ToDoItem.objects.get(item_id=item.id).update(status="completed")
            logging.info(f"Results from DB insert: {todo_item}")
            res = self.__make_todo_response(ToDoItem.objects.get(item_id=item.id))
            return res
        except Exception as e:
            logging.error(f"Error todo item: {e}")
            raise e



    def __make_todo_response(self, todo_item: ToDoItem) -> Dict[str,str]:
        return {"id": str(todo_item.item_id), "title": todo_item.title, "description": todo_item.description,
             "status": todo_item.status}


    def delete_todoItem(self, item: ItemDelete) -> Dict[str,str]:
        try:
            todo_item = ToDoItem.objects.get(item_id=item.id)
            todo_item.delete()
            logging.info(f"Results from DB insert: {todo_item}")
            return { "message": f"TODO item with ID '{item.id} has been deleted." }
        except Exception as e:
            logging.error(f"Error todo item: {e}")
            raise e