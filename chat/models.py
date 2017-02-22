# coding: utf-8
from __future__ import unicode_literals

from application.settings import AUTH_USER_MODEL
from django.db import models
from core.models import Authored, Titled, Dated

# Create your models here.

class Chat(Authored, Titled, Dated):
    subscribers = models.ManyToManyField(AUTH_USER_MODEL, related_name='subscribers')
    class Meta:
        verbose_name = u'Чат'
        verbose_name_plural = u'Чаты'

class Message(Authored, Dated):
    text = models.CharField(max_length = 300, blank = False)
    chat = models.ForeignKey(Chat, blank = False)
    class Meta:
        verbose_name = u'Сообщение'
        verbose_name_plural = u'Сообщения'
    
