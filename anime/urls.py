from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'anime'

router = SimpleRouter()
router.register(r'anime', views.AnimeViewSet)


urlpatterns = [
    
]

urlpatterns += router.urls
