import django_filters
from .models import Comment


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['user', 'anime']
    