from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100)
    profile_image_url = models.TextField(blank=True, null=True)
    location_lat = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    location_lng = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'               # 로그인 ID로 email 사용
    REQUIRED_FIELDS = ['username']         # createsuperuser 명령에서 필요

    def __str__(self):
        return self.email