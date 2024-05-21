from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


app_name = 'comment'

router = SimpleRouter()
router.register(r'', views.CommentViewSet)


urlpatterns = [
    
]

urlpatterns += router.urls
