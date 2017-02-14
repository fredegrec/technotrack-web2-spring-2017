# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import User, Authored

# Create your models here.
class Request(Authored):
    recipient = models.ForeignKey(User, blank = False, related_name = 'recipient')
    accepted = models.BooleanField(default=False)
    class Meta:
        verbose_name = u'Заявка в друзья'
        verbose_name_plural = u'Заявки в друзья'
    
class FriendShip(models.Model):
    first = models.ForeignKey(User, blank = False, related_name = 'first')
    second = models.ForeignKey(User, blank = False, related_name = 'second')
    class Meta:
        verbose_name = u'Друг'
        verbose_name_plural = u'Друзья'
    

