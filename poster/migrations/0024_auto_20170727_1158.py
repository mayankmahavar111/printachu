# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0023_auto_20170714_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poster',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='poster',
            name='image2',
            field=models.ImageField(default='', upload_to=b''),
        ),
        migrations.AddField(
            model_name='poster',
            name='image3',
            field=models.ImageField(default='', upload_to=b''),
        ),
    ]