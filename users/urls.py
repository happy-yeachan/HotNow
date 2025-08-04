from django.urls import path
from .views import MeView, UpdateLocationView

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('me/location', UpdateLocationView.as_view(), name='update_location'),
]