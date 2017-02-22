# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Authored
from application.settings import AUTH_USER_MODEL

# Create your models here.
class Request(Authored):
    recipient = models.ForeignKey(AUTH_USER_MODEL, blank = False, related_name = 'recipient')
    accepted = models.BooleanField(default=False)
    class Meta:
        verbose_name = u'Заявка в друзья'
        verbose_name_plural = u'Заявки в друзья'
    
class FriendShip(models.Model):
    first = models.ForeignKey(AUTH_USER_MODEL, blank = False, related_name = 'first')
    second = models.ForeignKey(AUTH_USER_MODEL, blank = False, related_name = 'second')
    class Meta:
        verbose_name = u'Друг'
        verbose_name_plural = u'Друзья'
    

