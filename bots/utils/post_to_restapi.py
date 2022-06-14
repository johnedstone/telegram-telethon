import requests

from utils.telethon_utils_v2 import (
    REST_API,
    REST_API_TOKEN,
)

HEADERS = {'Authorization': f'Token  {REST_API_TOKEN}'}

def post_to_restapi(logger_log, logger_error, data):
    try:
        logger_log.debug(data)

        r = requests.post(url=REST_API, headers=HEADERS, json=data)
        return r
    except Exception as e:
        logger_error.error(f'{e}')
        return f'post error: {e}'

def patch_username(logger_log, logger_error, data):
    try:
        return 'done'

        #r = requests.patch(url=REST_API, headers=HEADERS, json=data)
        #return r
    except Exception as e:
        logger_error.error(f'{e}')
        return f'patch error: {e}'

# vim: ai et ts=4 sw=4 sts=4 nu
