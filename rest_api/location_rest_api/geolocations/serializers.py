from rest_framework import serializers
from .models import Geolocation

#class GeolocationSerializer(serializers.HyperlinkedModelSerializer):
class GeolocationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('telegram_user', 'longitude', 'latitude', 'accuracy_radius')
        model = Geolocation

# vim: ai et ts=4 sw=4 sts=4 nu 
