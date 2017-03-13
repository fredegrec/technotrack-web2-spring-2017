# coding: utf-8
from __future__ import unicode_literals

from application.settings import AUTH_USER_MODEL
from django.db import models
from core.models import Authored, Titled, Dated

# Create your models here.

class Chat(Authored, Titled, Dated):
    subscribers = models.ManyToManyField(AUTH_USER_MODEL, related_name='inchat')
    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        
    def __unicode__(self):
        return self.title

class Message(Authored, Dated):
    text = models.CharField(max_length = 300, blank = False)
    chat = models.ForeignKey(Chat, blank = False, related_name='messages')
    
    def __unicode__(self):
        return '{0} написал {1}'.format(self.author.username, self.text)
        
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        
     
    
