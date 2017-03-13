from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Like
from .api import LikeSerializer
from application.api import router 
# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = permissions.IsAuthenticated,
    
    def get_queryset(self):
        qs = super(LikeViewSet, self).get_queryset()
        if 'author' in self.request.query_params:
            qs = qs.filter(author = self.request.query_params['author'])
        return qs
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)     
    
router.register('likes', LikeViewSet)