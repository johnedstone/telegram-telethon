import secrets
import string

from django.db import models

from core.models import TimeStampMixin

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
        randomized_id = ''.join(secrets.choice( 
               string.ascii_uppercase + string.digits) for i in range(16))
        # Next: check that this is unique
        telegramuser = self.create(username=username,
                randomized_id=randomized_id)

        return telegramuser


class TelegramUser(TimeStampMixin):
    username = models.CharField("Device", max_length=50, unique=True)
    randomized_id = models.CharField("Device", max_length=50, unique=True)

    objects = TelegramUserManager()

    def __str__(self):
        return self.username

# vim: ai et ts=4 sw=4 sts=4 nu 
