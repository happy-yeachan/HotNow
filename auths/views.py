from rest_framework import generics
from users.models import User
from auths.serializers import SignupSerializer

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer