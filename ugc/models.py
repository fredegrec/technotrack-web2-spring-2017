# coding: utf-8;
from __future__ import unicode_literals

from core.models import Authored, Titled, Dated
from events.models import Eventable
from likes.models import Likeable

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

        
class Comment(Authored, Dated, Likeable):
    text = models.CharField(max_length = 300, blank = False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
class Commentable(models.Model):
    comments = GenericRelation(Comment, content_type_field = 'content_type', object_id_field = 'object_id')
    
    class Meta:
        abstract = True
        
        
class Post(Authored, Titled, Dated, Likeable, Commentable, Eventable):
    text = models.TextField(max_length = 1000, blank = False)
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'