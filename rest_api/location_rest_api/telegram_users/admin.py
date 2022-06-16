from django.contrib import admin
from .models import TelegramUser

from core.helper_functions import get_random_id

class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'randomized_id', 'created_at',
            'updated_at')
    exclude = ('randomized_id',)

    def save_model(self, request, obj, form, change):
        obj.randomized_id = get_random_id()
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['username', 'user_id']
        return []


admin.site.register(TelegramUser, TelegramUserAdmin)
