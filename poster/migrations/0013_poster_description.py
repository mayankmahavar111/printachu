# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0012_category_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
