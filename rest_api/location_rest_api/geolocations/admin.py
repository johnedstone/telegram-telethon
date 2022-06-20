from django.contrib import admin
from .models import Geolocation

class GeolocationAdmin(admin.ModelAdmin):
    list_display = ('telegram_user', 'longitude', 'latitude', 'created_at',
            'bot', 'heading', 'period')
    list_filter = ('telegram_user__user_id', 'telegram_user__username', 'bot')

admin.site.register(Geolocation, GeolocationAdmin)
