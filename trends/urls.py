from django.urls import path
from .views import TrendListView
from .views import TrendListView, TrendDetailView

urlpatterns = [
    path('', TrendListView.as_view(), name='trend_list'),
    path('<int:pk>/', TrendDetailView.as_view(), name='trend_detail'),
]