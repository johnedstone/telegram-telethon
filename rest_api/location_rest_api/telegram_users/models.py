import logging
from django.db import models

from core.models import TimeStampMixin
from core.helper_functions import get_random_id

logger = logging.getLogger(__name__)

class TelegramUserManager(models.Manager):
    """Ref: https://docs.djangoproject.com/en/4.0/ref/models/instances/

    Using to create and check randomized_id
    Example:
    >>> from telegram_users.models import TelegramUser as TU
    >>> tu = TU.objects.create_telegramuser(user_id=1234568)
    >>> tu.randomized_id
    'uqcf9ye6c0bv7w74'
    >>> tu.full_clean()
    >>> tu.save()
    """

    def create_telegramuser(self, user_id, username=''):
        telegramuser = self.create(user_id=user_id, username=username,
                randomized_id=get_random_id())

        return telegramuser


class TelegramUser(TimeStampMixin):
    user_id = models.IntegerField('user_id', unique=True, blank=False)
    username = models.CharField('username', max_length=50,
            blank=True, default='')
    randomized_id = models.CharField('randomized id', max_length=50,
            unique=True, editable=False)

    objects = TelegramUserManager()

    def __str__(self):
        return f'{self.user_id}-{self.username}'

# vim: ai et ts=4 sw=4 sts=4 nu 
