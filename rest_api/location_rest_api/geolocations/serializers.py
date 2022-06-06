from rest_framework import serializers
from .models import Geolocation
from telegram_users.models import TelegramUser

#class GeolocationSerializer(serializers.HyperlinkedModelSerializer):
class GeolocationSerializer(serializers.ModelSerializer):

    """
    def to_internal_value(self, data):
        user_id = data.get('telegram_user')
        _ = TelegramUser.objects.get_or_create_telegram_user(user_id=user_id)

        return data
    """

    def create(self, validated_data):
        user_id = data.get('telegram_user')
        _ = TelegramUser.objects.get_or_create_telegram_user(user_id=user_id)

        return Geolocation.objects.create(**validated_data)

    class Meta:
        fields = ('telegram_user', 'longitude', 'latitude', 'accuracy_radius')
        model = Geolocation



# vim: ai et ts=4 sw=4 sts=4 nu 
