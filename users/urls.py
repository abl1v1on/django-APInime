from django.urls import path 

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter

from .views import CreateUserView, CustomTokenObtainPairView, ProfileViewSet


app_name = 'user'

router = SimpleRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('signup/', CreateUserView.as_view(), name='signup'),
]

urlpatterns += router.urls
