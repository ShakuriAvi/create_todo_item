from typing import Dict


def build_response(http_status:int, body: Dict[str,str]):
    return {
        "statusCode": http_status,
        "body": body
    }