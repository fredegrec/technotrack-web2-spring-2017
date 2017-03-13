# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Like(Authored, Dated):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together=(('author','content_type','object_id'),)
        
class Likeable(models.Model):
    likes = GenericRelation(Like, content_type_field = 'content_type', object_id_field = 'object_id')
    
    class Meta:
        abstract=True
    

        
        
        

