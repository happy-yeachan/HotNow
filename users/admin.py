from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'nickname', 'location_name', 'created_at']
    search_fields = ['email', 'nickname']