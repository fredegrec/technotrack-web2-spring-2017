# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Event(Authored, Dated):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'