# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0016_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='quora_count',
            field=models.IntegerField(default=0, max_length=10000),
        ),
        migrations.AddField(
            model_name='poster',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
