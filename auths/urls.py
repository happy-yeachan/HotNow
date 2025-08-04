from django.urls import path
from .views import SignupView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,       # 로그인용
    TokenRefreshView           # refresh token 처리용
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]