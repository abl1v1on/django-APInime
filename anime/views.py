from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AnimeSerializer, LikeSerializer, AnimeSeriesSerializer
from .filters import AnimeFilter, LikeFilter, AnimeSeriesFilter
from .utils import anime_utils, anime_series_urils, likes_utils
from .permissions import IsAdminUserOrReadOnly
from .models import Anime
from comments.utils import is_author


class AnimeViewSet(ModelViewSet):
    queryset = anime_utils.get_objects()
    serializer_class = AnimeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AnimeFilter
    ordering_fields = ['date_aired', 'title']    
    permission_classes = [IsAdminUserOrReadOnly]


class AnimeSeriesViewSet(ModelViewSet):
    queryset = anime_series_urils.get_objects()
    serializer_class = AnimeSeriesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnimeSeriesFilter
    permission_classes = [IsAdminUserOrReadOnly]


class LikeViewSet(ModelViewSet):
    queryset = likes_utils.get_objects()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LikeFilter   
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
