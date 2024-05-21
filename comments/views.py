from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CommentSerializer
from .models import Comment
from .filters import CommentFilter


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CommentFilter
    ordering_fields = ['date_created', 'comment_text']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        print(request.method)
        try:
            if Comment.objects.get(pk=kwargs['pk']).user != request.user:
                return Response({'detal': 'Доступ запрещен'}, status=400)
        except Comment.DoesNotExist:
            return Response({'detail': 'Объект не найден'})
        return super().retrieve(request, *args, **kwargs)
