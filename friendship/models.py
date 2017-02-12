from __future__ import unicode_literals

from django.db import models
from core.models import User, Authored

# Create your models here.
class Request(Authored):
    recipient = models.ForeignKey(User, related_name = 'recipient')
    accepted = models.BooleanField(default=False)
    
class FriendShip(models.Model):
    first = models.ForeignKey(User, related_name = 'first')
    second = models.ForeignKey(User, related_name = 'second')
    

