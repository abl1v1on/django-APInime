from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import CustomTokenObtainPairSerializer, CreateUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny, )
