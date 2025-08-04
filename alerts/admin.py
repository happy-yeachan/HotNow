from django.contrib import admin
from .models import UserAlertSetting

@admin.register(UserAlertSetting)
class UserAlertSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
