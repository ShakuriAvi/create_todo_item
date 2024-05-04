from parameterized import parameterized
import unittest
from tests.unit_test.abstract_tast import AbstractUnitTest
from tests.unit_test.utils import read_test_config, factory, parameterized_test
from pydantic import ValidationError
from typing import Dict
import json

def read_test_config(action: str, input_path: str):
    with open(input_path) as fp:
        test_config = json.load(fp)
    inputs_items = test_config.get(action, {}).get("inputs", [])
    for input_item in inputs_items:
        yield input_item

class TestGet(AbstractUnitTest, unittest.TestCase):
    @parameterized_test("get_action", 'tests/unit_test/test_config.json')
    def test_input_validation_type(self, inputs: Dict[str, str]):
        try:
            item = factory["get_action"]
            item(**inputs)
        except Exception as exc:
            assert False
        assert True


if __name__ == '__main__':
    unittest.main()
