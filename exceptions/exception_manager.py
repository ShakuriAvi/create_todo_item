from typing import Dict, Any

from starlette.exceptions import HTTPException

class BaseHttpException(HTTPException):
    status_code: int = None
    detail: str = None
    headers: Dict[str, Any] = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail, headers=self.headers)

class UncorrectedInputException(BaseHttpException):
    status_code = 400
    detail = 'Invalid Input'

class EnvException(BaseHttpException):
    status_code = 513
    detail = 'get_environment_variables was called before init_environment_variables, environment variables were not loaded'