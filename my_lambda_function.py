import sys
import os
from http import HTTPStatus
from typing import Any, Dict, Callable
from aws_lambda_powertools.utilities.parser import ValidationError, parse
from aws_lambda_powertools.utilities.parser.envelopes import ApiGatewayEnvelope
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.middleware_factory import lambda_handler_decorator
from entities.schemas import MyHandlerEnvVars
from entities.schemas import Item
from handler.utils.env_vars_parser import get_environment_variables, init_environment_variables
from handler.utils.http_responses import build_response
from handler.handler_request import HandlerRequest
from exceptions.exception_manager import EnvException

import logging
sys.path.append(os.path.dirname(__file__))


@lambda_handler_decorator
def middleware_before(
        handler: Callable[[Item, LambdaContext], dict],
        event: dict,
        context: LambdaContext,
) -> dict:
    try:
        item: Item = parse(event=event, model=Item)
        logging.info('got create request', extra={'order_item_count': item.title})
    except ValidationError as exc:
        logging.error('event failed input validation', extra={'error': str(exc)})
        return build_response(http_status=int(HTTPStatus.BAD_REQUEST), body={})

    response = handler(item, context)

    return response


@init_environment_variables(model=MyHandlerEnvVars)
@middleware_before
def my_handler(event: Item, context: LambdaContext) -> Dict[str, Any]:
    try:
        logging.info('my_handler is called, calling inner_function_example')
        env_vars = get_environment_variables()
        logging.debug('environment variables', extra=env_vars.dict())
        handler_request = HandlerRequest(env_vars)
        handler_response = handler_request.create_new_item(event)
        logging.info('inner_function_example finished successfully')

    except EnvException as e:
        return build_response(e.status_code, e.detail)

    except Exception as e:
        logging.error('Failed.', exc_info=e)
        return build_response(500, {"status": "error occurs"})

    return build_response(http_status=int(HTTPStatus.OK), body=handler_response)
