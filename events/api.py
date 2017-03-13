from rest_framework import serializers, permissions

from .models import Event
from core.api import UserSerializer
from friendship.api import FriendShipSerializer
from friendship.models import FriendShip
from friendship.api import FriendShipSerializer
from ugc.api import PostSerializer
from ugc.models import Post

class ContentObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Post):
            serializer = PostSerializer(value)
        elif isinstance(value, FriendShip):
            serializer=FriendShipSerializer(value)
        else:
            raise Exception("Unexpected type of object")
        return serializer.data

class EventSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created_time = serializers.ReadOnlyField()
    content_object = ContentObjectRelatedField(read_only=True)
    
    class Meta:
        model = Event
        fields = ('id', 'author', 'content_object', 'created_time', )
