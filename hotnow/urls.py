from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('auths.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/trends/', include('trends.urls')),
    path('api/v1/alerts/', include('alerts.urls')),
]