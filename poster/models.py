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

class CustomerProfile(models.Model):
    user=models.ForeignKey(User)
    Curr_status=models.CharField(default="",max_length=100)
    email=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.user

class ArtistProfile(models.Model):
    user=models.ForeignKey(User)
    name=models.CharField(max_length=50,default='')
    profile_pic=models.ImageField(default='')
    Description=models.CharField(max_length=400,default='')
    designs_no=models.IntegerField(default=0)
    cash_rec=models.IntegerField(default=0)
    cash_nrec=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Category(models.Model):
    user=models.ForeignKey(User)
    name=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name

class poster(models.Model):
    name=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(default="",max_length=100)
    image=models.ImageField(default="")

    def __str__(self):
        return self.description


