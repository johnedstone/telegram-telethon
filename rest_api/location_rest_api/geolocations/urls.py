from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'geolocations', views.GeolocationViewSet)

# vim: ai et ts=4 sw=4 sts=4 nu 
