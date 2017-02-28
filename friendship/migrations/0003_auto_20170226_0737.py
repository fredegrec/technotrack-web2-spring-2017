# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 07:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friendship', '0002_auto_20170214_0942'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('first', 'second')]),
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=set([('author', 'recipient')]),
        ),
    ]