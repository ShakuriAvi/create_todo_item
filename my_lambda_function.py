import sys
import os
sys.path.append(os.path.dirname(__file__))
if True:
    from http import HTTPStatus
    from typing import Any, Dict
    from entities.schemas import MyHandlerEnvVars
    from handler.utils.env_vars_parser import get_environment_variables, init_environment_variables
    from handler.utils.http_responses import build_response
    from handler.handler_request import HandlerRequest
    from exceptions.exception_manager import EnvException
    from middlewere.logic import middleware_before
    import logging


@init_environment_variables(model=MyHandlerEnvVars)
@middleware_before
def create_handler(event, context) -> Dict[str, Any]:
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
        return build_response(500, {'error': "error occurs"})

    return build_response(http_status=int(HTTPStatus.OK), body=handler_response)


@init_environment_variables(model=MyHandlerEnvVars)
@middleware_before
def get_handler(event, context) -> Dict[str, Any]:
    try:
        logging.info('my_handler is called, calling inner_function_example')
        env_vars = get_environment_variables()
        logging.debug('environment variables', extra=env_vars.dict())
        handler_request = HandlerRequest(env_vars)
        handler_response = handler_request.get_item(event)
        logging.info(f'inner_function_example finished successfully {handler_response}')

    except EnvException as e:
        return build_response(e.status_code, e.detail)

    except Exception as e:
        logging.error('Failed.', exc_info=e)
        return build_response(500, {'error': str(e)})

    return build_response(http_status=int(HTTPStatus.OK), body=handler_response)

@init_environment_variables(model=MyHandlerEnvVars)
@middleware_before
def put_handler(event, context) -> Dict[str, Any]:
    try:
        logging.info('my_handler is called, calling inner_function_example')
        env_vars = get_environment_variables()
        logging.debug('environment variables', extra=env_vars.dict())
        handler_request = HandlerRequest(env_vars)
        handler_response = handler_request.update_item(event)
        logging.info(f'inner_function_example finished successfully {handler_response}')

    except EnvException as e:
        return build_response(e.status_code, e.detail)

    except Exception as e:
        logging.error('Failed.', exc_info=e)
        return build_response(500, {'error': str(e)})

    return build_response(http_status=int(HTTPStatus.OK), body=handler_response)

@init_environment_variables(model=MyHandlerEnvVars)
@middleware_before
def delete_handler(event, context) -> Dict[str, Any]:
    try:
        logging.info('my_handler is called, calling inner_function_example')
        env_vars = get_environment_variables()
        logging.debug('environment variables', extra=env_vars.dict())
        handler_request = HandlerRequest(env_vars)
        handler_response = handler_request.delete_item(event)
        logging.info(f'inner_function_example finished successfully {handler_response}')

    except EnvException as e:
        return build_response(e.status_code, e.detail)

    except Exception as e:
        logging.error('Failed.', exc_info=e)
        return build_response(500, {'error': str(e)})

    return build_response(http_status=int(HTTPStatus.OK), body=handler_response)