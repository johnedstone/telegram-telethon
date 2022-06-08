from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'telegram-users', views.TelegramUserViewSet)

# vim: ai et ts=4 sw=4 sts=4 nu 

