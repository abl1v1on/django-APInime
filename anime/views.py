from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from .serializers import AnimeSerializer, LikeSerializer, AnimeSeriesSerializer
from .filters import AnimeFilter, LikeFilter, AnimeSeriesFilter
from .utils import anime_series_urils, likes_utils, get_all_anime, get_likes
from .permissions import IsAdminUserOrReadOnly
from .models import Anime
from .paginations import AnimeListAPIViewPagination
from comments.utils import is_author


class AnimeViewSet(ModelViewSet):
    queryset = get_all_anime()
    serializer_class = AnimeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AnimeFilter
    ordering_fields = ['date_aired', 'title', 'likes_count']    
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = AnimeListAPIViewPagination


class AnimeSeriesViewSet(ModelViewSet):
    queryset = anime_series_urils.get_objects()
    serializer_class = AnimeSeriesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AnimeSeriesFilter
    ordering_fields = ['series_number']    
    permission_classes = [IsAdminUserOrReadOnly]


class LikeViewSet(ModelViewSet):
    queryset = get_likes()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LikeFilter   
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = is_author(self.get_object(), request)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        anime_id = self.request.data.get('anime')
        anime = get_object_or_404(Anime, pk=anime_id)
        if likes_utils.is_exist(user=self.request.user, anime=anime):
            raise ValidationError(detail='You have already liked this anime')
        serializer.validated_data['user'] = self.request.user
        serializer.save()
