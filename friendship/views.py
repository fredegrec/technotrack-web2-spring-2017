from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Request, FriendShip
from .api import RequestSerializer, FriendShipSerializer
from application.api import router 
# Create your views here.
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = permissions.IsAuthenticated,
    
    def get_queryset(self):
        qs = super(RequestViewSet, self).get_queryset()
        if 'author' in self.request.query_params:
            qs = qs.filter(author = self.request.query_params['author'])
        if 'recipient' in self.request.query_params:
            qs=qs.filter(recipient=self.request.query_params['recipient'])
        return qs
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)     
    
router.register('requests', RequestViewSet)

class FriendShipViewSet(viewsets.ModelViewSet):
    queryset = FriendShip.objects.all()
    serializer_class = FriendShipSerializer
    permission_classes = permissions.IsAuthenticated,
    
    def get_queryset(self):
        qs = super(FriendShipViewSet, self).get_queryset()
        if 'user' in self.request.query_params:
            qs = qs.filter(first = self.request.query_params['user'])
        return qs
    
    def perform_create(self, serializer):
        serializer.save(first=self.request.user)     
    
router.register('friends', FriendShipViewSet)