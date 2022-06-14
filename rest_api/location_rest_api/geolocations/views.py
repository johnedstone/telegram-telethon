import logging
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as filters

from .models import Geolocation
from .permissions import GeolocationPermissions

from .serializers import (
    GeolocationSerializer,
    GeolocationSerializerRandomizedDataOnly,
    GeolocationSerializerCanPost,
    GeolocationSerializerViewAllData,
)

logger = logging.getLogger(__name__)


class GeolocationFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    telegram_user_user_id = filters.NumberFilter(field_name='telegram_user', lookup_expr="user_id__exact")
    telegram_user_username = filters.CharFilter(field_name='telegram_user', lookup_expr="username__exact")
    telegram_user_randomized_id = filters.CharFilter(field_name='telegram_user', lookup_expr="randomized_id__exact")

    class Meta:
        model = Geolocation
        fields = ['created_at', 'telegram_user']


class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    permission_classes = [GeolocationPermissions]
    ordering_fields = ['created_at']
    filterset_class = GeolocationFilter

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

    def perform_create(self, serializer):
        serializer.save(bot=self.request.user)

# vim: ai et ts=4 sw=4 sts=4 nu 
