import requests

from utils.telethon_utils_v2 import (
    REST_API,
    REST_API_TOKEN,
)

def post_to_restapi(logger_log, logger_error, data):
    try:
        logger_log.debug(data)

        headers = {'Authorization': f'Token  {REST_API_TOKEN}'}
        r = requests.post(url=REST_API, headers=headers, json=data)
        return r
    except Exception as e:
        logger_error.error(f'{e}')
        return f'{e}'

