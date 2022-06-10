from rest_framework import viewsets
from .models import TelegramUser
from .permissions import TelegramUserPermissions
from .serializers import (
        TelegramUserSerializer,
        TelegramUserSerializerRandomized,
        TelegramUserSerializerPatch,
        TelegramUserSerializerViewAll,
)

class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    permission_classes = [TelegramUserPermissions]
    serializer_class = TelegramUserSerializer
    ordering_fields = [
        'randomized_id',
        'username',
        'user_id',
    ]

    def get_serializer_class(self, *args, **kwargs):
        user = self.request.user

        if user.is_superuser:
            return TelegramUserSerializer

        elif user.has_perm('geolocations.can_view_randomized_data_only'):
            return TelegramUserSerializerRandomized

        elif user.has_perm('geolocations.can_post_geolocation'):
            return TelegramUserSerializerPatch

        elif user.has_perm('geolocations.can_view_all_data'):
            return TelegramUserSerializerViewAll

        else:
            raise PermissionDenied


# vim: ai et ts=4 sw=4 sts=4 nu
