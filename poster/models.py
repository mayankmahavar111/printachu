from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models


class UserProfile(models.Model):
    user=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_birth=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)
    email=models.EmailField()
    join_as=models.CharField(max_length=10)

    def __str__(self):
        return self.user


