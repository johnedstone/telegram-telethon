import logging
import json
import os
import sys

from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

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
