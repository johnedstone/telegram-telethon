import logging
from django.db import models

from core.models import TimeStampMixin
from telegram_users.models import TelegramUser

class Geolocation(TimeStampMixin):

    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE,
            blank=False)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    accuracy_radius = models.IntegerField(blank=True, null=True)

    @property
    def randomized_id(self):
        return self.telegram_user.randomized_id

    def __str__(self):
        return f'{self.randomized_id}-{self.created_at}-{self.longitude:.5f}-{self.latitude:.5f}'
