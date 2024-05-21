from django.urls import path 

from rest_framework_simplejwt.views import TokenRefreshView

from .views import CreateUserView, CustomTokenObtainPairView

app_name = 'user'


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('signup/', CreateUserView.as_view(), name='signup'),
]
