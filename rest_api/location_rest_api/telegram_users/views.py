from rest_framework import viewsets
from .models import TelegramUser
from .serializers import TelegramUserSerializer

class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer

    """Reference: https://www.cdrf.co/3.13/rest_framework.viewsets/ModelViewSet.html

    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    http --json patch  http://localhost:8000/api/v1/telegram-users/2/ username='boohoo'
    """
    http_method_names = ['get', 'patch', 'head', 'options']

# vim: ai et ts=4 sw=4 sts=4 nu
