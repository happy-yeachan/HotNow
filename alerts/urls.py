from django.urls import path
from .views import UserAlertSettingListCreateView, UserAlertSettingDetailView

urlpatterns = [
    path('', UserAlertSettingListCreateView.as_view(), name='alert-list-create'),
    path('<int:id>/', UserAlertSettingDetailView.as_view(), name='alert-detail'),
]
