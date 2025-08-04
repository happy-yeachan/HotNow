from rest_framework import generics, permissions
from .models import User
from .serializers import UserProfileSerializer, UserLocationUpdateSerializer

class MeView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # 인증된 유저 객체 반환

class UpdateLocationView(generics.UpdateAPIView):
    serializer_class = UserLocationUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # 로그인한 사용자 본인