from django.db import models

class TrendKeyword(models.Model):
    CATEGORY_CHOICES = [
        ('restaurant', '맛집'),
        ('date', '데이트'),
        ('exhibition', '전시'),
        ('activity', '체험'),
        ('travel', '여행'),
    ]

    SOURCE_CHOICES = [
        ('sns', 'SNS'),
        ('community', '커뮤니티'),
        ('news', '뉴스'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.category})'