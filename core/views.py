from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .api import UserSerializer
from .permissions import IsOwnerOrReadOnly
from application.api import router

from django.contrib.auth import get_user_model

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    
        
router.register('users', UserViewSet)