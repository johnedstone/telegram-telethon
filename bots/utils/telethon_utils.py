import logging
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession


env_file = os.getenv('LIST_UPTIMES_ENV', '.env')
load_dotenv(env_file)

log_to_file = os.getenv('LOG_TO_FILE') == 'yes'

log_path =os.getenv('LIST_UPTIMES_LOG', '')
error_path = os.getenv('LIST_UPTIMES_ERROR', '')

logger_log = logging.getLogger('logs')
logger_error = logging.getLogger('errors')

logger_log.setLevel(logging.INFO)
logger_error.setLevel(logging.WARNING)

formatter = logging.Formatter(fmt="%(asctime)s [%(levelname)s]: %(message)s")

if log_to_file and Path(log_path).is_file() and Path(error_path).is_file():
    handler_log = logging.FileHandler(log_path)
    handler_error = logging.FileHandler(error_path)

else:
    handler_log = logging.StreamHandler(stream=sys.stdout)
    handler_error = logging.StreamHandler(stream=sys.stderr)

handler_log.setFormatter(formatter)
handler_error.setFormatter(formatter)


logger_log.addHandler(handler_log)
logger_error.addHandler(handler_error)

def start_bot(prod=True):
    bot_token = os.getenv('TOKEN_LIST_UPTIMES_BOT')
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    rest_api = os.getenv('REST_API')
    params = os.getenv('PARAMS')

    for ea in [api_id, api_hash, bot_token, rest_api, params]:
        if not ea:

            logger_error.error('''
                First set environment variables: {}
            '''.format(ea))
            sys.exit()

    try:
        bot = TelegramClient(StringSession(), api_id, api_hash).start(bot_token=bot_token)
    except Exception as e:
        logger_error.error('''
            Starting bot error, exiting: {}
        '''.format(e))
        sys.exit()

    return bot, rest_api, json.loads(params)


# vim: ai et ts=4 sw=4 sts=4 nu
