from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Event
from .api import EventSerializer
from application.api import router 
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = permissions.IsAuthenticated,
    
    def get_queryset(self):
        qs = super(EventViewSet, self).get_queryset()
        if 'author' in self.request.query_params:
            qs = qs.filter(author = self.request.query_params['author'])
        return qs
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)     
    
router.register('events', EventViewSet)