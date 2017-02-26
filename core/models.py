# coding: utf-8
from __future__ import unicode_literals

from application.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
        
        
class Authored(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL)
    
    class Meta:
        abstract = True
        
        
class Titled(models.Model):
    title = models.CharField(max_length = 100, blank = True)
    
    class Meta:
        abstract = True
        
        
class Dated(models.Model):
    created_time =  models.DateField(auto_now_add = True)
    
    class Meta:
        abstract = True
        
