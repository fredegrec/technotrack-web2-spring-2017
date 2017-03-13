from rest_framework import serializers, permissions

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', )

