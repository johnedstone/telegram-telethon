import logging
from rest_framework import serializers
from .models import TelegramUser

logger = logging.getLogger(__name__)

class TelegramUserSerializer(serializers.HyperlinkedModelSerializer):
    """Using for superuser"""


    class Meta:
        fields = (
                'updated_at',
                'created_at',
                'randomized_id',
                'url',
                'username',
                'user_id',
        )
        model = TelegramUser

class TelegramUserSerializerPatch(serializers.HyperlinkedModelSerializer):


    class Meta:
        fields = (
                'updated_at',
                'url',
                'username',
                'user_id',
        )
        model = TelegramUser


# vim: ai et ts=4 sw=4 sts=4 nu 
