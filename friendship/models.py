# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Authored
from events.models import Eventable
from application.settings import AUTH_USER_MODEL

# Create your models here.
class Request(Authored):
    recipient = models.ForeignKey(AUTH_USER_MODEL, blank = False, related_name = 'recipient')
    accepted = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Заявка в друзья'
        verbose_name_plural = 'Заявки в друзья'
        unique_together = (('author', 'recipient'),)
    
class FriendShip(Eventable):
    first = models.ForeignKey(AUTH_USER_MODEL, blank = False, related_name = 'first')
    second = models.ForeignKey(AUTH_USER_MODEL, blank = False, related_name = 'second')
    
    def get_author(self):
        return self.first
    
    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'
        unique_together = (('first', 'second'),)
    

