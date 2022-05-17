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
log_path =os.getenv('LIST_UPTIMES_LOG')
error_path = os.getenv('LIST_UPTIMES_ERROR')

if log_to_file and Path(log_path).is_file() and Path(error_path).is_file():
    formatter = logging.Formatter(fmt="%(asctime)s [%(levelname)s]: %(message)s")

    handler_log_file = logging.FileHandler(log_path)
    handler_error_file = logging.FileHandler(error_path)

    handler_log_file.setFormatter(formatter)
    handler_error_file.setFormatter(formatter)

    logger_log_file = logging.getLogger('logs')
    logger_error_file = logging.getLogger('errors')

    logger_log_file.setLevel(logging.INFO)
    logger_error_file.setLevel(logging.WARNING)

    logger_log_file.addHandler(handler_log_file)
    logger_error_file.addHandler(handler_error_file)

    loggers = (logger_log_file, logger_error_file)
else:
    pass
    "write stdout stderr loggers here"

def start_logging(logging_level=logging.INFO):
    #logging_level = logging.INFO
    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging_level
    )
    return logging.getLogger(__name__)

def start_bot(prod=True):
    bot_token = os.getenv('TOKEN_LIST_UPTIMES_BOT')
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    rest_api = os.getenv('REST_API')
    params = os.getenv('PARAMS')

    for ea in [api_id, api_hash, bot_token, rest_api, params]:
        if not ea:

            sys.exit('''
                First set environment variables: {}
            '''.format(ea))

    try:
        bot = TelegramClient(StringSession(), api_id, api_hash).start(bot_token=bot_token)
    except Exception as e:
        sys.exit('''
            Starting bot error, exiting: {}
        '''.format(e))

    return bot, rest_api, json.loads(params)


# vim: ai et ts=4 sw=4 sts=4 nu
