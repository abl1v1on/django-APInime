from rest_framework import serializers

from .models import Anime, Studio, Like

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['id', 'slug']


class AnimeSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    views = serializers.IntegerField(read_only=True)
    studio = StudioSerializer()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Anime
        fields = '__all__'
    
    def get_likes(self, obj: Anime):
        return obj.total_likes()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
    