from rest_framework import serializers

from .models import Anime, Studio, Genre

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['id', 'slug']


class AnimeSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    views = serializers.IntegerField(read_only=True)
    studio = StudioSerializer()

    class Meta:
        model = Anime
        fields = '__all__'