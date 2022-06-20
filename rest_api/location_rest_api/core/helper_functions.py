import logging
import secrets
import string

from telegram_users import models as tu_models

logger = logging.getLogger(__name__)

def get_random_id():
    """Returns unique, random id

    Checks first to make sure that the random_id does not already exist
    as 'randominzed_id'.  If so, try again, until a unique random_id is
    generated.

    See also: https://humberto.io/blog/tldr-generate-django-secret-key/
    >>> secrets.token_urlsafe(12)
    '9kOQ6M_r9k0MHnps'
    >>> len(secrets.token_urlsafe(12))
    16
    """

    not_unique = True

    while not_unique:
        #random_id = ''.join(secrets.choice(
        #       string.ascii_uppercase.replace('O', '').replace('I', '') + \
        #               string.digits.replace('0', '').replace('1', '')) for i in range(16))
        random_id = secrets.token_urlsafe(12)

        try:
            _ = tu_models.TelegramUser.objects.get(randomized_id__exact=random_id)
            logger.info('Exists! Try again!! Get another random id')
        except tu_models.TelegramUser.DoesNotExist as e:
            logger.info(f'{random_id} is random!!')
            not_unique = False

    return random_id

# vim: ai et ts=4 sw=4 sts=4 nu
