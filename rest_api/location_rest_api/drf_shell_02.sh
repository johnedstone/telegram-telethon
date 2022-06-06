from telegram_users.models import TelegramUser as TU
from geolocations.serializers import GeolocationSerializer as GS
from geolocations.models import Geolocation as G 
import io
from rest_framework.parsers import JSONParser

for ea in TU.objects.all():
    print(ea, ea.user_id, ea.id)
serializer = GS(G.objects.all(), many=True)
print(serializer.data)

# vim: ai et ts=4 sts=4 sw=4 nu

