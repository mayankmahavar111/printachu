# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0025_artistprofile_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistprofile',
            name='cart',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cart',
            field=models.CharField(default='', max_length=1000),
        ),
    ]