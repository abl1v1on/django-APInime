import django_filters
from .models import Anime, Genre, Studio, Like, AnimeSeries


class AnimeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    genres = django_filters.ModelMultipleChoiceFilter(
        field_name='genres__slug',
        queryset=Genre.objects.all(),
        to_field_name='slug'
    )
    studio = django_filters.ModelChoiceFilter(
        queryset=Studio.objects.all(), 
        field_name='studio__name'
    )

    class Meta:
        model = Anime
        fields = ['title', 'genres', 'studio']


class AnimeSeriesFilter(django_filters.FilterSet):
    class Meta:
        model = AnimeSeries
        fields = ['anime_id']


class LikeFilter(django_filters.FilterSet):
    class Meta:
        model = Like
        fields = ['anime', 'user']
    