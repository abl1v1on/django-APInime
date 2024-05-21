from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AnimeSerializer
from .filters import AnimeFilter
from .utils import utils
from .permissions import IsAdminUserOrReadOnly


class AnimeViewSet(ModelViewSet):
    queryset = utils.get_anime()
    serializer_class = AnimeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AnimeFilter
    ordering_fields = ['date_aired', 'title', 'likes']    
    permission_classes = [IsAdminUserOrReadOnly]


# class LikeViewSet(ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = LikeFilter
#     # ordering_fields = ['date_aired', 'title']    
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def create(self, request, *args, **kwargs):
#         if request.data:
#             if Like.objects.filter(
#                 user_id=request.data['user'], 
#                 anime_id=request.data['anime']
#             ).exists():
#                 return Response({'detail': 'It\'s already been liked.'})
#         return super().create(request, *args, **kwargs)
