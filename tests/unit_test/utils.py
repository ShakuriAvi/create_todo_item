from entities.schemas import ItemCreate, ItemPut, ItemDelete, ItemGet
from unittest import mock
import os
import json


def mockenv(**envvars):
    for k, v in envvars.items():
        os.environ[k] = v
    return mock.patch.dict(os.environ, envvars)


def read_test_config(action: str, input_path: str):
    with open(input_path) as fp:
        test_config = json.load(fp)
    inputs_items = test_config[action]["inputs"]
    env_config = test_config["environ"]
    mockenv(**env_config)
    for input_item in inputs_items:
        yield input_item

def parameterized_test(action: str, input_path: str):
    def decorator(test_method):
        def wrapper(self):
            for input_item in read_test_config(action, input_path):
                with self.subTest(input_item=input_item):
                    test_method(self, input_item)
        return wrapper
    return decorator

factory = {
    "create_action": ItemCreate,
    "put_action": ItemPut,
    "del_action": ItemDelete,
    "get_action": ItemGet
}