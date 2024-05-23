from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'anime'

anime_router = SimpleRouter()
anime_router.register(r'anime', views.AnimeViewSet)
anime_router.register(r'episodes', views.AnimeSeriesViewSet, basename='anime-series')


like_router = SimpleRouter()
like_router.register(r'likes', views.LikeViewSet)

# anime_series_router = SimpleRouter()
# anime_series_router.register(r'episodes', views.AnimeSeriesViewSet)


urlpatterns = [

]

urlpatterns += anime_router.urls
urlpatterns += like_router.urls
