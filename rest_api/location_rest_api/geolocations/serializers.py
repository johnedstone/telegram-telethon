import logging
from .models import Geolocation
from .mixins import GeolocationSerializerBase

logger = logging.getLogger(__name__)

class GeolocationSerializer(GeolocationSerializerBase):
    """Using for superuser"""

    class Meta:
        model = Geolocation
        fields = (
                'telegram_user', # need to set up url pattern to include this
                'telegram_user_username',
                'telegram_user_user_id',
                'telegram_username_posted',
                'telegram_user_randomized_id',
                'longitude',
                'latitude',
                'accuracy_radius',
                'heading',
                'period',
                'created_at',
                )

class GeolocationSerializerRandomizedDataOnly(GeolocationSerializerBase):

    class Meta:
        model = Geolocation
        fields = (
                'telegram_user',
                'telegram_user_randomized_id',
                'longitude',
                'latitude',
                'accuracy_radius',
                'heading',
                'period',
                'created_at',
                )

class GeolocationSerializerCanPost(GeolocationSerializerBase):

    class Meta:
        model = Geolocation
        fields = (
                #'telegram_user_randomized_id',
                'telegram_user',
                'telegram_username_posted',
                'longitude',
                'latitude',
                'accuracy_radius',
                'heading',
                'period',
                #'created_at',
                )

class GeolocationSerializerViewAllData(GeolocationSerializerBase):

    class Meta:
        model = Geolocation
        fields = (
                'telegram_user',
                'telegram_user_username',
                'telegram_user_user_id',
                'telegram_username_posted',
                'telegram_user_randomized_id',
                'longitude',
                'latitude',
                'accuracy_radius',
                'heading',
                'period',
                'created_at',
                )

# vim: ai et ts=4 sw=4 sts=4 nu 
