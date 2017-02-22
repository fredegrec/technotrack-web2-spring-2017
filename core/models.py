# coding: utf-8
from __future__ import unicode_literals

from application.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(u'Имя', max_length = 30, blank = True)
    last_name = models.CharField(u'Фамилия', max_length = 30, blank = True)
    username = models.CharField(u'Логин', max_length = 20, blank = False, unique = True)
    email = models.EmailField(u'e-mail', blank = False, unique = True)
    
    
    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        
        
        
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
        
