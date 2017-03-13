from rest_framework import serializers, permissions

from .models import Message, Chat
from core.api import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    
    class Meta:
        model = Message
        fields = ('id', 'author', 'text', 'chat', 'created_time', )


class ChatSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    subscribers=UserSerializer(many=True)
    messages = MessageSerializer(many=True, read_only = True)
    
    class Meta:
        model = Chat
        fields = ('id', 'author', 'title', 'created_time', 'subscribers', 'messages', )