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

def get_logger(logger_name, logging_level=logging.INFO,
        logging_error_level=logging.WARNING):

    logger_log = logging.getLogger(logger_name)
    logger_error = logging.getLogger(logger_name + '_errors')


    logger_log.setLevel(logging_level)
    logger_error.setLevel(logging_error_level)

    formatter = logging.Formatter(fmt="%(asctime)s %(name)s:%(lineno)d [%(levelname)s]: %(message)s")
    
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

    logger_log.debug(f'{logger_log.name}')
    logger_error.debug(f'{logger_error.name}')
 
    return logger_log, logger_error

def start_bot(prod=True):
    logger_log, logger_error = get_logger(__name__)

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

    logger_log.info('bot has started')
    return bot, rest_api, json.loads(params)


# vim: ai et ts=4 sw=4 sts=4 nu