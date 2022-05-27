from django.contrib import admin
from .models import TelegramUser

class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'randomized_id')



admin.site.register(TelegramUser, TelegramUserAdmin)
