from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Post
from .api import PostSerializer
from application.api import router 
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = permissions.IsAuthenticated,
    
    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        if 'author' in self.request.query_params:
            qs = qs.filter(author = self.request.query_params['author'])
        return qs
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)     
    
router.register('posts', PostViewSet)