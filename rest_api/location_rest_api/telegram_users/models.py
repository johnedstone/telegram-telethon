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
    >>> tu = TU.objects.create_telegramuser(username="manonman")
    >>> tu.randomized_id
    'uqcf9ye6c0bv7w74'
    >>> tu.full_clean()
    >>> tu.save()
    """

    def create_telegramuser(self, username):
        telegramuser = self.create(username=username,
                randomized_id=get_random_id())

        return telegramuser


class TelegramUser(TimeStampMixin):
    username = models.CharField('username', max_length=50,
            unique=True, blank=False)
    randomized_id = models.CharField('randomized id', max_length=50,
            unique=True, blank=False, editable=False)
    # add telegram_id

    objects = TelegramUserManager()

    def __str__(self):
        return self.username

# vim: ai et ts=4 sw=4 sts=4 nu 
