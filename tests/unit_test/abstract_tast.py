from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Dict

class AbstractUnitTest(ABC):
    @abstractmethod
    def test_input_validation_type(self, inputs: Dict[str, str]):
        pass