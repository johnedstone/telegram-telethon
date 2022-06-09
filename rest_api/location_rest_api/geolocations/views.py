from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import Geolocation
from .serializers import GeolocationSerializer

class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        user = self.request.user
        return GeolocationSerializer
        """Set globally
        if user.is_authenticated:
            return GeolocationSerializer
        else:
            raise PermissionDenied
        """


# vim: ai et ts=4 sw=4 sts=4 nu 
