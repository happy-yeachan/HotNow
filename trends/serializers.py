from rest_framework import serializers
from trends.models import TrendKeyword

class TrendKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendKeyword
        fields = ['id', 'name', 'category', 'score', 'latitude', 'longitude']