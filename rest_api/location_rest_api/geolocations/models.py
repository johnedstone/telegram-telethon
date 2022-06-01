import logging
from django.db import models

from core.models import TimeStampMixin

class Geolocation(TimeStampMixin):

    @property
    def randomized_id(self):
        return self.user_id.randomized_id

    def __str__(self):
        return f'{randomized_id}-{created_at}-{long:.5f}-{lat:.5f}'
