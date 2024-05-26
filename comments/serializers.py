from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='user.pk'
    )
    
    class Meta:
        model = Comment
        fields = '__all__'

