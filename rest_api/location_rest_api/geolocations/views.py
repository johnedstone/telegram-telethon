import logging
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import Geolocation
from .permissions import GeolocationPermissions

from .serializers import (
    GeolocationSerializer,
    GeolocationSerializerRandomizedDataOnly,
    GeolocationSerializerCanPost,
    GeolocationSerializerViewAllData,
)

logger = logging.getLogger(__name__)

class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    permission_classes = [GeolocationPermissions]

    def get_serializer_class(self, *args, **kwargs):
        user = self.request.user

        if user.is_superuser:
            return GeolocationSerializer

        elif user.has_perm('geolocations.can_view_randomized_data_only'):
            return GeolocationSerializerRandomizedDataOnly

        elif user.has_perm('geolocations.can_post_geolocation'):
            return GeolocationSerializerCanPost

        elif user.has_perm('geolocations.can_view_all_data'):
            return GeolocationSerializerViewAllData

        else:
            raise PermissionDenied


# vim: ai et ts=4 sw=4 sts=4 nu 
