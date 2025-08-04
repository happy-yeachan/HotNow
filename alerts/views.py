from rest_framework import generics, permissions
from alerts.models import UserAlertSetting
from alerts.serializers import UserAlertSettingSerializer

class UserAlertSettingListCreateView(generics.ListCreateAPIView):
    serializer_class = UserAlertSettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserAlertSetting.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAlertSettingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserAlertSettingSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return UserAlertSetting.objects.filter(user=self.request.user)
