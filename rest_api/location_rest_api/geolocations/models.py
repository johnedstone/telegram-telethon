import logging
from django.db import models

from core.models import TimeStampMixin
from telegram_users.models import TelegramUser

logger = logging.getLogger(__name__)

class Geolocation(TimeStampMixin):

    class Meta:
        permissions = [
            ("can_view_randomized_data_only", "Can view randomized data only"),
            ("can_view_all_data", "Can view all data"),
            ("can_post_geolocation", "Can post geolocation"),
        ]
        ordering = ['-created_at']

    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE,
            blank=False)#, related_name='geolocation_telegram_user')
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    accuracy_radius = models.PositiveIntegerField(blank=True, null=True)
    heading = models.PositiveIntegerField(blank=True, null=True)
    period = models.PositiveIntegerField(blank=True, null=True)

    @property
    def telegram_user_randomized_id(self):
        return self.telegram_user.randomized_id

    @property
    def telegram_user_username(self):
        return self.telegram_user.username

    @property
    def telegram_user_user_id(self):
        return self.telegram_user.user_id

    @property
    def telegram_username_posted(self):
        if self.telegram_user.username:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.telegram_user_randomized_id}-{self.created_at}-{self.longitude:.5f}-{self.latitude:.5f}'

# vim: ai et ts=4 sw=4 sts=4 nu
