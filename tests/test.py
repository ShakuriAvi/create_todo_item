import unittest
from parameterized import parameterized
import json
from my_lambda_function import get_handler, create_handler, put_handler
from unittest import mock
import os


def mockenv(**envvars):
    for k, v in envvars.items():
        os.environ[k] = v
    return mock.patch.dict(os.environ, envvars)


def read_test_config(action: str):
    with open('test_config.json') as fp:
        test_config = json.load(fp)
    inputs_items = test_config[action]["inputs"]
    output_item = test_config[action]["expected_output"]
    env_config = test_config["environ"]
    mockenv(**env_config)
    for input_item in inputs_items:
        yield input_item, output_item


class TestSequence(unittest.TestCase):

    # @parameterized.expand(read_test_config("create_action"))
    # def test_create(self,  input_item, output_item):
    #     assert create_handler(input_item, bunchify({'function_name': 'create_todo_item'}))["statusCode"] > output_item

    # @parameterized.expand(read_test_config("get_action"))
    # def test_get(self,  input_item, output_item):
    #     context = {'function_name': 'get_todo_item'}
    #     assert get_handler(input_item, type('new_dict', (object,), context))["statusCode"] > output_item

    @parameterized.expand(read_test_config("get_action"))
    def test_put(self,  input_item, output_item):
        context = {'function_name': 'put_todo_item'}
        assert put_handler(input_item, type('new_dict', (object,), context))["statusCode"] > output_item




if __name__ == '__main__':
    unittest.main()