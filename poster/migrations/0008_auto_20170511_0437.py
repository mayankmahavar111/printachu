# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0007_artistprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='artistprofile',
            name='profile_pic',
            field=models.FileField(default='', upload_to=b''),
        ),
    ]
