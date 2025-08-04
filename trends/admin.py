from django.contrib import admin
from .models import TrendKeyword, TrendEventLog

@admin.register(TrendKeyword)
class TrendKeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'score', 'created_at']
    list_filter = ['category', 'source_type']

@admin.register(TrendEventLog)
class TrendEventLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'keyword', 'source_type', 'mention_count', 'event_time']
