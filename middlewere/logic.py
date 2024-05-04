from aws_lambda_powertools.utilities.parser import ValidationError, parse
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.middleware_factory import lambda_handler_decorator
from entities.schemas import ItemCreate, ItemGet, ItemPut, ItemDelete
from typing import Callable
from pydantic import BaseModel
import logging
from handler.utils.http_responses import build_response
from http import HTTPStatus

models_object = {
    "get_todo_item": ItemGet,
    "create_todo_item": ItemCreate,
    "put_todo_item": ItemPut,
    "delete_todo_item": ItemDelete
}


@lambda_handler_decorator
def middleware_before(
        handler: Callable[[BaseModel, LambdaContext], dict],
        event: dict,
        context: LambdaContext,
) -> dict:
    try:
        print(vars(context), event)
        logging.info(f"middleware get: {vars(context)}, {event}")
        if event.get("pathParameters"):
            for k, v in event.get("pathParameters").items():
                event[k] = v
        item: BaseModel = parse(event=event, model=models_object[context.function_name])
        logging.info('got create request', extra={'order_item_count': item.id})
    except ValidationError as exc:
        logging.error('event failed input validation', extra={'error': str(exc)})
        return build_response(http_status=int(HTTPStatus.BAD_REQUEST), body={'error': str(exc)})

    response = handler(item, context)

    return response
