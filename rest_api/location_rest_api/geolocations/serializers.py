import logging
from rest_framework import serializers
from .models import Geolocation
from telegram_users.models import TelegramUser

logger = logging.getLogger(__name__)

#class GeolocationSerializerBase(serializers.ModelSerializer): # developed with this
class GeolocationSerializerBase(serializers.HyperlinkedModelSerializer):
    """
    A base serializer (Mixin) to be used by the following serializers
    """

    def to_internal_value(self, data):

        logger.info(data)
        for ea in ['telegram_user', 'longitude', 'latitude']:
            if ea not in data:
                logger.info(f'{ea} is required.')
                raise serializers.ValidationError({
                    ea: f'{ea} is required.'
                })
            else:
                if ea == 'telegram_user':
                    if not isinstance(data[ea], int):
                        logger.info(f'{ea} is not an integer. It is a {type(data[ea])}')
                        raise serializers.ValidationError({
                            ea: f'{ea} is not an integer. It is a {type(data[ea])}'
                        })
                    else:
                        logger.info(f'{ea} is an integer. It is a {type(data[ea])}')
                if ea in ['longitude', 'latitude']:
                    if not isinstance(data[ea], float):
                        logger.info(f'{ea} is not an float. It is a {type(data[ea])}')
                        raise serializers.ValidationError({
                            ea: f'{ea} is not an float'
                        })
                    else:
                        logger.info(f'{ea} is an float. It is a {type(data[ea])}')

        user_id = data.pop('telegram_user')

        telegram_user = TelegramUser.objects.get_or_create_telegram_user(user_id=user_id)

        data['telegram_user'] = telegram_user

        return data

class GeolocationSerializer(GeolocationSerializerBase):

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
                'created_at',
                'telegram_user_pk',
                )

# vim: ai et ts=4 sw=4 sts=4 nu 
