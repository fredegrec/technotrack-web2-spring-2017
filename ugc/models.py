# coding: utf-8;
from __future__ import unicode_literals

from core.models import Authored, Titled, Dated
from likes.models import Likeable

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

        
class Comment(Authored, Dated, Likeable):
    text = models.CharField(max_length = 300, blank = False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        
class Commentable(models.Model):
    comments = GenericRelation(Comment, content_type_field = 'content_type', object_id_field = 'object_id')
    
    class Meta:
        abstract = True
        
        
class Post(Authored, Titled, Dated, Likeable, Commentable):
    text = models.TextField(max_length = 1000, blank = False)
    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'