from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsChatSubscriber, IsOwnerOrReadOnly
from .models import Message, Chat
from .api import MessageSerializer, ChatSerializer
from application.api import router 
# Create your views here.
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, IsChatSubscriber, )
    
    def get_queryset(self):
        qs = super(ChatViewSet, self).get_queryset()
        if 'username' in self.request.query_params:
            qs = qs.filter(subscribers__username = self.request.query_params['username'])
        return qs
    
    def perform_create(self, serializer):
        chat = serializer.save(author=self.request.user)   
        chat.subscribers.add(self.request.user)
        chat.save()
        
    #def perform_update(self, serializer):
        
           
router.register('chats', ChatViewSet)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    
    def get_queryset(self):
        qs = super(MessageViewSet, self).get_queryset()
        if 'author' in self.request.query_params:
            qs = qs.filter(author = self.request.query_params['author'])
        if 'chat' in self.request.query_params:
            qs = qs.filter(chat = self.request.query_params['chat'])
        return qs
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
router.register('messages', MessageViewSet)