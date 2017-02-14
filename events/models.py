# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated
from post.models import Post
from friendship.models import Request
from likes.models import Like
from chat.models import Chat
# Create your models here.
class Event(Authored, Dated):
    post = models.ForeignKey(Post)
    request = models.ForeignKey(Request)
    like = models.ForeignKey(Like)
    chat = models.ForeignKey(Chat)
    
    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

