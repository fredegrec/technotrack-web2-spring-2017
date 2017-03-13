from rest_framework import serializers, permissions

from .models import FriendShip, Request
from core.api import UserSerializer


class RequestSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    #recipient=serializers.ReadOnlyField(source='recipient.id')
    
    class Meta:
        model = Request
        fields = ('id', 'author', 'recipient', 'accepted', )
        
class FriendShipSerializer(serializers.ModelSerializer):
    first = serializers.ReadOnlyField(source='first.id')
    second=serializers.ReadOnlyField(source='second.id')
    
    class Meta:
        model = Request
        fields = ('id', 'first', 'second', )
