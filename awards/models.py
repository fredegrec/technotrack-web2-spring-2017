# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from application.settings import AUTH_USER_MODEL
from core.models import Titled, Dated

# Create your models here.
class Award(Titled, Dated):
    description=models.CharField(max_length=300, blank=False)
    recipient=models.ForeignKey(AUTH_USER_MODEL)
    class Meta:
        verbose_name='Награда'
        verbose_name_plural='Награды'
        

       
    