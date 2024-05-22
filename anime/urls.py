from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'anime'

anime_router = SimpleRouter()
anime_router.register(r'anime', views.AnimeViewSet)

like_router = SimpleRouter()
like_router.register(r'likes', views.LikeViewSet)

urlpatterns = [
    # path('like/', views.LikeCreateAPIView.as_view(), name='like'),
    # path('like-delete/', views.DeleteLikeAPIView.lookup_field, name='like_delete'),
]

urlpatterns += anime_router.urls
urlpatterns += like_router.urls
