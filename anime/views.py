from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AnimeSerializer, LikeSerializer, AnimeSeriesSerializer
from .filters import AnimeFilter, LikeFilter
from .utils import utils
from .permissions import IsAdminUserOrReadOnly
from .models import Anime, Like, AnimeSeries


class AnimeViewSet(ModelViewSet):
    queryset = utils.get_anime()
    serializer_class = AnimeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AnimeFilter
    ordering_fields = ['date_aired', 'title']    
    permission_classes = [IsAdminUserOrReadOnly]


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LikeFilter   
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.data:
            if Like.objects.filter(
                user_id=request.data['user'], 
                anime_id=request.data['anime']
            ).exists():
                return Response({'detail': 'It\'s already been liked.'})
        return super().create(request, *args, **kwargs)


class AnimeSeriesAPIVIew(APIView):
    def get(self, request):
        try:
            episodes = AnimeSeries.objects.filter(anime_id=request.data['anime'])
            serializer = AnimeSeriesSerializer(episodes, many=True)
            return Response(serializer.data, status=200)
        except KeyError:
            return Response({'anime': ['This is a required field']})
    