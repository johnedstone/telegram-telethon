#!/usr/bin/env python
"""Telegram bot to list nicely formated data from a REST API"""

from datetime import datetime
import logging
import re

import requests

from telethon import events, Button
from telethon_utils import start_logging, start_bot


logger = start_logging(logging_level=logging.WARNING)
bot, rest_api, params = start_bot()
bot.parse_mode = 'md'

p = re.compile(r'Start time .unixtime . utc_datetime.: \d+ .')
pz = re.compile(r'(.\d{6}Z|.\d{6}\+00:00)$')

keyboard = [
    Button.inline('Post a report', b'5'),
    Button.inline('List recent uptimes (/list)', b'6'),
]

def format_dict(result_dict):
    results = ''
    for ea in result_dict.keys():
        results = results + '**{}**\n'.format(ea)
        counter = 0
        result_dict[ea].reverse()
        for ea_ea in result_dict[ea]:
            results = results + '  {}\n'.format(ea_ea)
            counter += 1
            if counter == 4:
                break
        results = results + '\n'

    return results

def get_uptime_report():
    """query the REST API"""
    results = {}
    r = requests.get(url=rest_api, params=params)
    if r.ok:
        data = r.json()
        for ea in data['results']:
            if ea['arduino_name'] not in results:
                results[ea['arduino_name']] = [] 

            results[ea['arduino_name']].insert(0, f"""created: {pz.sub('', ea["created_at"])}
    {pz.sub('', p.sub('uptime: ', ea["uptime"]))}""")

    results = format_dict(results)
    results = results + f"""**Currently:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"""

    logger.info(results)
    return f'{results}'


@bot.on(events.CallbackQuery(data=re.compile(r'5')))
async def handler(event):
    logger.info('{}'.format(dir(event)))
    logger.info('{}'.format(event.stringify()))
    await event.respond('__Coming soon!__')
    ## sometime try:
    ## await event.respond('__Coming soon!__', parse_mode='md')
    ## and remove bot.parse_mode above

@bot.on(events.CallbackQuery(data=re.compile(r'6')))
async def handler(event):
    logger.info('{}'.format(dir(event)))
    logger.info('{}'.format(event.stringify()))
    await event.respond(get_uptime_report())
    await event.respond('Choose an option', buttons=keyboard)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """https://stackoverflow.com/questions/61184048/how-to-position-and-resize-button-in-telegram-using-telethon"""
    await bot.send_message(event.chat_id, "Choose an option:", buttons=keyboard)

@bot.on(events.NewMessage(pattern='/list'))
async def list(event):
    await event.respond(get_uptime_report())
    await event.respond('Choose an option', buttons=keyboard)
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond('Use /start to show choices')
    await event.respond('Use /list to show uptimes')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()

# vim: ai et ts=4 sw=4 sts=4 nu
