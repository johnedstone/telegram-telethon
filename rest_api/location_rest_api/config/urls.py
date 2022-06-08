from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import redirect


from rest_framework.routers import DefaultRouter
from geolocations.urls import router as geolocation_router
from telegram_users.urls import router as telegram_user_router

router = DefaultRouter()
router.registry.extend(geolocation_router.registry)
router.registry.extend(telegram_user_router.registry)


urlpatterns = [
    url(r'^$', lambda x: redirect('/api/v1/', permanent=False), name='home'),
    path('geolocations-admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
]

# vim: ai et ts=4 sw=4 sts=4 nu 
