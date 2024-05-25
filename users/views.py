from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Profile
from .serializers import CustomTokenObtainPairSerializer, CreateUserSerializer, ProfileSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny, )


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'put', 'patch']

    def update(self, request, *args, **kwargs):
        profile = self.get_object()

        if profile.user.pk == request.user.pk:
            return super().update(request, *args, **kwargs)
        else:
            return Response({'detail': 'Access denied'}, status=400)
    