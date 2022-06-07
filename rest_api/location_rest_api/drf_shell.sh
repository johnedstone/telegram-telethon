print("Usage: python manage.py shell < drf_shell.sh")
from geolocations.serializers import GeolocationSerializer
import io
from rest_framework.parsers import JSONParser

#content = b'{"telegram_user": 6953 , "longitude": 7.4, "latitude": 9.5, "accuracy_radius": 5}'
content = b'{"telegram_user": 69536953 , "longitude": 7.3, "latitude": 0.0}'
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
gs = GeolocationSerializer(data=data)
print(gs)
print(gs.is_valid())
#print(dir(gs))
if gs.is_valid():
    print(gs.validated_data)
    print(gs.save())
