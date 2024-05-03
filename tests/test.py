import unittest
from parameterized import parameterized
import json
from my_lambda_function import my_handler
from unittest import mock
import os

def mockenv(**envvars):
    for k,v in envvars.items():
        os.environ[k] = v
    return mock.patch.dict(os.environ, envvars)

def read_test_config():
    with open('tests/test_config.json') as fp:
        test_config = json.load(fp)
    inputs_items = test_config["inputs"]
    output_item = test_config["expected_output"]
    env_config = test_config["environ"]
    mockenv(**env_config)
    for input_item in inputs_items:
        yield input_item, output_item

class TestSequence(unittest.TestCase):

    @parameterized.expand(read_test_config())
    def test_sequence(self,  input_item, output_item):
        assert my_handler(input_item, {})["statusCode"] > output_item


if __name__ == '__main__':
    unittest.main()