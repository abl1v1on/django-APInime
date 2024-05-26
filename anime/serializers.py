from rest_framework import serializers

from .models import Anime, Studio, Like, AnimeSeries, Genre


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['id', 'slug']


class AnimeSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeSeries
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class AnimeSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    views = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField()
    studio = StudioSerializer()
    genres = GenreSerializer(many=True)
    
    class Meta:
        model = Anime
        exclude = ('likes', )


class AnimeSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'title']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='user.pk'
    )

    class Meta:
        model = Like
        fields = '__all__'
