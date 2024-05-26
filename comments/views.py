from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CommentSerializer
from .models import Comment
from .filters import CommentFilter
from .utils import is_author


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.prefetch_related('user', 'anime').all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CommentFilter
    ordering_fields = ['date_created', 'comment_text']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = is_author(self.get_object(), request)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = is_author(self.get_object(), request)
        self.perform_update(instance)
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()
        