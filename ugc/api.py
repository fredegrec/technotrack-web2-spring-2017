from rest_framework import serializers, permissions

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    
    class Meta:
        model = Post
        fields = ('text', 'author', 'title', )

