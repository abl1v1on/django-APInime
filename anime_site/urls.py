from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anime.urls', namespace='anime')),
    path('users/', include('users.urls', namespace='user')),
    path('comments/', include('comments.urls', namespace='comment'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    