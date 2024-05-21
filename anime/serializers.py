from rest_framework import serializers

from .models import Anime, Studio

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
        print(Anime.likes)
        print('\n\n\n')
        return obj.total_likes()


class LikeSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    anime = serializers.IntegerField()

