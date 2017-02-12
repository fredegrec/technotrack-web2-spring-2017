from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Titled, Dated

# Create your models here.

class Chat(Authored, Titled, Dated):
    pass

class Message(Authored, Dated):
    text = models.CharField(max_length = 300, blank = False)
    chat = models.ForeignKey(Chat)
    
