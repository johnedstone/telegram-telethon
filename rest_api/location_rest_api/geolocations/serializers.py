import logging
from rest_framework import serializers
from .models import Geolocation
from telegram_users.models import TelegramUser

logger = logging.getLogger(__name__)

#class GeolocationSerializer(serializers.HyperlinkedModelSerializer):
class GeolocationSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('telegram_user', 'longitude', 'latitude', 'accuracy_radius')
        model = Geolocation


    def to_internal_value(self, data):
        #logger.debug(help(data))

        logging.debug(data)
        user_id = data.pop('telegram_user')
        logging.debug(data)

        telegram_user = TelegramUser.objects.get_or_create_telegram_user(user_id=user_id)

        data['telegram_user'] = telegram_user
        logging.debug(data)

        return data

# vim: ai et ts=4 sw=4 sts=4 nu 
