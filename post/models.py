from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Titled, Dated

# Create your models here.
class Post(Authored, Titled, Dated):
    text = models.CharField(max_length = 1000, blank = False)
    
    