from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from decimal import Decimal

from payments import PurchasedItem
from payments.models import BasePayment

class UserProfile(models.Model):
    user=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_birth=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)
    email=models.EmailField()
    join_as=models.CharField(max_length=10)
    cart=models.CharField(max_length=1000,default=' ')

    def __str__(self):
        return self.user

class CustomerProfile(models.Model):
    user=models.ForeignKey(User)
    Curr_status=models.CharField(default="",max_length=100)
    email=models.CharField(max_length=100,default='')
    cart=models.CharField(max_length=1000,default='')



class ArtistProfile(models.Model):
    user=models.ForeignKey(User)
    name=models.CharField(max_length=50,default='')
    profile_pic=models.ImageField(default='')
    background_pic=models.ImageField(default='')
    Description=models.CharField(max_length=400,default='')
    designs_no=models.IntegerField(default=0)
    cash_rec=models.IntegerField(default=0)
    cash_nrec=models.IntegerField(default=0)
    about =models.CharField(max_length=1000,default=' ')

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name

class poster(models.Model):
    user=models.ForeignKey(User)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(default="",max_length=100)
    image1=models.ImageField(default="")
    image2=models.ImageField(default="")
    image3=models.ImageField(default="")
    title=models.CharField(default='',max_length=100)
    quora_count=models.IntegerField(default=0)


    def __str__(self):
        return self.title

class tags(models.Model):
    title=models.CharField(default="anything",max_length=100)
    poster_name=models.CharField(default=" ",max_length=5000)

    def __str__(self):
        return self.title



class Payment(BasePayment):

    def get_failure_url(self):
        return 'http://example.com/failure/'

    def get_success_url(self):
        return 'http://example.com/success/'

    def get_purchased_items(self):
        # you'll probably want to retrieve these from an associated order
        yield PurchasedItem(name='The Hound of the Baskervilles', sku='BSKV',
                            quantity=9, price=Decimal(10), currency='USD')



