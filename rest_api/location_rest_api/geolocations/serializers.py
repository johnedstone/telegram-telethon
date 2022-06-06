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

    def create(self, validated_data):
        user_id = data.get('telegram_user')
        _ = TelegramUser.objects.get_or_create_telegram_user(user_id=user_id)

        return Geolocation.objects.create(**validated_data)
    """
    #telegram_user = serializers.PrimaryKeyRelatedField(queryset=TelegramUser.objects.all())
    #telegram_user = serializers.StringRelatedField(read_only=False)

    class Meta:
        fields = ('telegram_user', 'longitude', 'latitude', 'accuracy_radius')
        model = Geolocation


    """
    def create(self, validated_data):
        user_id = validated_data.pop('telegram_user')
        telegram_user = TelegramUser.objects.get_or_create_telegram_user(user_id=user_id)
        print(telegram_user)
        geolocation=Geolocation(telegram_user=telegram_user, **validated_data)

        return geolocation
    """

    def to_internal_value(self, data):
        user_id = data.get('telegram_user')
        telegram_user = TelegramUser.objects.get_or_create_telegram_user(user_id=user_id)

        return {
            'telegram_user': telegram_user,
            'latitude': 4.5,
            #'longitude': 6.0,
        }


# vim: ai et ts=4 sw=4 sts=4 nu 
