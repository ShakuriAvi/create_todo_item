from mongoengine import Document, StringField, DateTimeField, SequenceField
from datetime import datetime
from pydantic import BaseModel, constr, Field


class Item(BaseModel):
    title: constr(min_length=1, max_length=20)
    description: constr(min_length=1)


class ToDoItem(Document):
    meta = {
        'collection': 'todos_items'
    }
    item_id = SequenceField()
    title = StringField()
    description = StringField()
    status = StringField(default="pending")
    created_at = DateTimeField(default=datetime.utcnow)

class MyHandlerEnvVars(BaseModel):
    TODOS_DBNAME: constr(min_length=1)
    HOST: constr(min_length=1)


