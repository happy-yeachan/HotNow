from rest_framework import serializers
from alerts.models import UserAlertSetting

class UserAlertSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAlertSetting
        fields = ['id', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
