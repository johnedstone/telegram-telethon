from rest_framework import viewsets
from .models import TelegramUser
from .serializers import TelegramUserSerializer
from .permissions import TelegramUserPermissions

class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    permission_classes = [TelegramUserPermissions]
    serializer_class = TelegramUserSerializer

    def get_serializer_class(self, *args, **kwargs):
        user = self.request.user

        if user.is_superuser:
            return TelegramUserSerializer

        elif user.has_perm('geolocations.can_view_randomized_data_only'):
            raise PermissionDenied

        elif user.has_perm('geolocations.can_post_geolocation'):
            return TelegramSerializerPatch

        elif user.has_perm('geolocations.can_view_all_data'):
            raise PermissionDenied

        else:
            raise PermissionDenied


# vim: ai et ts=4 sw=4 sts=4 nu
