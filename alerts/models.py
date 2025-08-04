from django.db import models
from users.models import User

class UserAlertSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - alert active: {self.is_active}"
