from django.contrib import admin
from .models import TelegramUser

class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'randomized_id')
    readonly_fields = ('randomized_id', 'created_at',
            'updated_at')


admin.site.register(TelegramUser, TelegramUserAdmin)
