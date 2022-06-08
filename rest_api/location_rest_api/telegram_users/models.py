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
    >>> tu = TU.objects.create_telegram_user(user_id=1234568)
    >>> tu.randomized_id
    'uqcf9ye6c0bv7w74'
    >>> tu.full_clean()
    >>> tu.save()


    Someday explore this: https://gist.github.com/carymrobbins/7223141
    """

    def create_telegram_user(self, user_id, username=''):
        telegram_user = self.create(user_id=user_id, username=username,
                randomized_id=get_random_id())

        return telegram_user

    def get_or_create_telegram_user(self, user_id, username=''):
        try:
            telegram_user = TelegramUser.objects.get(user_id=user_id)
        except TelegramUser.DoesNotExist:
            telegram_user = self.create(user_id=user_id, username=username,
                    randomized_id=get_random_id())

        return telegram_user


class TelegramUser(TimeStampMixin):

    class Meta:
        ordering = ['created_at']

    user_id = models.PositiveIntegerField('user_id', unique=True, blank=False)
    username = models.CharField('username', max_length=50,
            blank=True, default='')
    randomized_id = models.CharField('randomized id', max_length=50,
            unique=True, editable=False)

    objects = TelegramUserManager()

    def __str__(self):
        return f'{self.user_id}-username_unknown'
        return f'{self.user_id}-{self.username}'
        return f'{self.user_id}'

# vim: ai et ts=4 sw=4 sts=4 nu 
