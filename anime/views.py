from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
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
    ordering_fields = ['date_aired', 'title']    
    permission_classes = [IsAdminUserOrReadOnly]
