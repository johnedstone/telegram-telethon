from django.db import models

from core.models import TimeStampMixin

class TelegramUsers(TimeStampMixin):
    name = models.CharField("Device", max_length=50, unique=True)
    randomized_id = models.CharField("Device", max_length=50, unique=True)

    def __str__(self):
        return self.name

# vim: ai et ts=4 sw=4 sts=4 nu 
