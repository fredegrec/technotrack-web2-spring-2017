from rest_framework import serializers, permissions

from .models import Post
from likes.api import LikeableSerializer

class PostSerializer(LikeableSerializer):
    author = serializers.ReadOnlyField(source='author.id')
  
    
    class Meta:
        model = Post
        fields = ('text', 'author', 'title', 'likes', 'likes_count', )

