from rest_framework import serializers, permissions

from .models import Likeable, Like
#from ugc.api import PostSerializer


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created_time=serializers.ReadOnlyField()
    #content_object = serializers.ReadOnlyField(source='post.id')
    
    class Meta:
        model = Like
        fields = ('author', 'created_time', 'content_type', 'object_id', )

class LikeableSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    likes = LikeSerializer(many=True, read_only=True)
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    
    
    
    