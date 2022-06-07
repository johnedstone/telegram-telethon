from django.urls import path, include
from rest_framework.routers import DefaultRouter
from geolocations import views

router = DefaultRouter()
router.register(r'geolocations', views.GeolocationViewSet,basename="geolocation")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
