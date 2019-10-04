# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from account.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.core import serializers
import json
from django.http import  HttpResponse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey('Category',null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name

class AdsQuerySet(models.query.QuerySet): #for active
    def active(self):
        return self.filter(active=True)

class AdsManager(models.Manager):#for active
    def get_queryset(self):
        return AdsQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()
# Create your models here.


class Ads(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    ad_title =models.CharField( max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=0,max_digits=30)
    description = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    ad_image = models.ImageField(upload_to='ads/',default='profile/None/no-img.jpg')
    active = models.BooleanField(default=True)
    # deleted = models.BooleanField(default=False,null=True, blank=True)
    # disabled =  models.BooleanField(default=False,null=True, blank=True)
    objects = AdsManager()#for active

    def __str__(self):
        return self.ad_title


class AdsImages(models.Model):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    ad_image = models.ImageField(upload_to='ads/', verbose_name=_('Photo'), default='profile/None/no-img.jpg')
