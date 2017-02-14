# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated
from post.models import Post

# Create your models here.
class Like(Authored, Dated):
    post = models.ForeignKey(Post)

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки' 