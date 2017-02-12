# coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(u'Имя', max_length = 30, blank = True)
    last_name = models.CharField(u'Фамилия', max_length = 30, blank = True)
    username = models.CharField(u'Логин', max_length = 20, blank = False, unique = True)
    email = models.EmailField(u'e-mail', blank = False, unique = True)
    
    
    class Meta:
        verbose_name = u'пользователь'
        verbose_name_plural = u'пользователи'
        
        
        
class Authored(models.Model):
    author = models.ForeignKey(User)
    
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
        
