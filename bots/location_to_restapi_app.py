#!/usr/bin/env python

import logging
import re

from telethon import events, Button, utils
from utils.telethon_utils_v2 import start_bot, get_logger
from utils.post_to_restapi import post_to_restapi, patch_username

logger_log, logger_error = get_logger(logging_level=logging.INFO)

bot = start_bot('TOKEN_LOCATION_BOT', logger_log, logger_error)

""" Use to figure out what kind of message is 'coming in'

@bot.on(events.Raw)
async def handler(event):
    logger_log.warning(f'''What is this event:
    {event}''')
    logger_log.warning('#' * 50)
"""

async def get_username(user_id):

    user = await bot.get_entity(user_id)

    username = utils.get_display_name(user)
    logger_log.debug(username)

    return username

@bot.on(events.MessageEdited)
async def handler(event):
    if event.geo:
        logger_log.debug('Yes, an updated geo object')

        # To do: send post to create this user
        # if already created do not get_entity

        # To do: figure out when this is stopped
        # https://core.telegram.org/api/live-location
        user = await bot.get_entity(event.message.peer_id) # could be expensive

        logger_log.debug(f'{event.message}')

        logger_log.debug(f'event: {event}')
        msg = (
            #f'{utils.get_display_name(user)}'
            #f' | {event.edit_date} | '
            f'{event.media.geo.long}'
            f' | {event.media.geo.lat}'
            f' | accuracy radius: {event.media.geo.accuracy_radius if event.media.geo.accuracy_radius else ""}'
            f' | heading: {event.media.heading if event.media.heading else ""}'
            f' | period: {event.media.period if event.media.period else ""}'
            )
        
        logger_log.debug(msg)
        data = {
                'telegram_user': event.peer_id.user_id,
                'longitude': event.media.geo.long,
                'latitude': event.media.geo.lat,
        }
        accuracy_radius = event.media.geo.accuracy_radius
        if accuracy_radius:
            data['accuracy_radius'] = accuracy_radius

        heading = event.media.heading
        if heading:
            data['heading'] = heading

        period = event.media.period
        if period:
            data['period'] = period

        try:
            response = post_to_restapi(logger_log, logger_error, data)
            if response.status_code == 201:
                logger_log.debug(response.text)
            else:
                logger_error.error(f'Posting this geolocation event failed: {response.status_code} status code')
        except Exception as e:
            logger_error.warning(f'MessageEdited: posting to restapi error: {e}')
        ##

@bot.on(events.NewMessage)
async def handler(event):
    if event.geo:
        logger_log.debug('Yes, a geo object')

        # To do: send post to create this user
        # if already created do not get_entity
        user = await bot.get_entity(event.message.peer_id)

        logger_log.debug(f'event: {event}')
        logger_log.debug(f'{event.message}')
        logger_log.debug(f'dir(event.message): {dir(event.message)}')
        logger_log.debug(f'event.media.geo: {event.media.geo}')
        logger_log.debug(f'{event.date}')

        """Not sure of the diffence:

        await bot.send_message(event.chat_id, "Thanks, we know where you are!")
        """
        await event.respond("Thanks, we know where you are!")

        msg = (
            #f'{utils.get_display_name(user)}'
            #f' | {event.edit_date} | '
            f'{event.media.geo.long}'
            f' | {event.media.geo.lat}'
            f' | accuracy radius: {event.media.geo.accuracy_radius if event.media.geo.accuracy_radius else ""}'
            ## Sometimes this is absent in the MessageMediaGeo
            #f' | heading: {event.media.heading if event.media.heading else ""}'
            #f' | period: {event.media.period if event.media.period else ""}'
            )
 
        logger_log.debug(msg)

        data = {
                'telegram_user': event.peer_id.user_id,
                'longitude': event.media.geo.long,
                'latitude': event.media.geo.lat,
        }

        accuracy_radius = event.media.geo.accuracy_radius
        if accuracy_radius:
            data['accuracy_radius'] = accuracy_radius

        try:
            response = post_to_restapi(logger_log, logger_error, data)
            if response.status_code == 201:
                logger_log.debug(response.text)

                response_dict = response.json()
                if not response_dict['telegram_username_posted']:
                    username = await get_username(event.peer_id.user_id)

                    username_response = patch_username(logger_log, logger_error,
                            url=response_dict['telegram_user'],
                            data={"username": username})
                    logger_log.debug(
                        f'''{username_response.status_code}, {username_response.text}''')

                else:
                    logger_log.debug('username has been posted, no need to patch the username')

            else:
                logger_error.error(f'Posting this geolocation event failed: {response.status_code} status code')
        except Exception as e:
            logger_error.warning(f'NewMessage: posting to restapi error: {e}')

    else:
        logger_log.debug('No, not a geo object')
        logger_log.debug(f'event: {event}')
        #await bot.send_message(event.chat_id, "Yikes! we're sure what you are saying")

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """https://stackoverflow.com/questions/61184048/how-to-position-and-resize-button-in-telegram-using-telethon"""

    """ Not using
    await bot.send_message(event.chat_id, "Send Location __(below)__ or Select Live Tracking __(as usual)__", buttons=keyboard, parse_mode='md')
    """
    await bot.send_message(event.chat_id, "Select __Share my Live Location for ...__", parse_mode='md')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'))
async def help(event):
    #await event.respond('Use /start to show choices')
    await bot.send_message(event.chat_id, "/start for more info", parse_mode='md')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()

# vim: ai et ts=4 sw=4 sts=4 nu
