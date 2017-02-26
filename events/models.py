# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.
class Event(Authored, Dated):
    content = models.TextField(max_length=500, blank=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        
        
class Eventable(models.Model):
    events = GenericRelation(Event, content_type_field = 'content_type', object_id_field = 'object_id')
    
    class Meta:
        abstract = True
        
