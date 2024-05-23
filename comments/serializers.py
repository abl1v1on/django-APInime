from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True
    )
    
    class Meta:
        model = Comment
        fields = '__all__'

