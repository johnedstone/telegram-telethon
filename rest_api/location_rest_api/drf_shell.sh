print("Usage: python manage.py shell < drf_shell.sh")
from geolocations.serializers import GeolocationSerializer
import io
from rest_framework.parsers import JSONParser

#content = b'{"telegram_user": "2233445555", "longitude": "4.4", "latitude": 5.5}'
content = b'{"telegram_user": 1, "longitude": "4.4", "latitude": 5.5}'
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
gs = GeolocationSerializer(data=data)
print(gs)
print(gs.is_valid())
