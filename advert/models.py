# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from account.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.core import serializers
import json
from django.http import  HttpResponse
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:ads_list_by_category',
                       args=[self.slug])

class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lga(models.Model):
    state = models.ForeignKey('State',null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Offer(models.Model):
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
    AGE = (
        ('05', '0-5 Years'),
        ('10', '0-10 Years'),
        ('15', '0-15 Years'),
        ('20', '0-20 Years'),
        ('21', '20+ Years'),)

    BEDROOMS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'More than 5'),)

    BATHROOMS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'More than 5'),)

    ROOMS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', 'More than 5'),)

    PERIOD = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),)

    CONDITION = (
        ('new', 'New'),
        ('old', 'Old'),
        ('uncompleted', 'Uncompleted'),
        ('renovated', 'Renovated'),)

    LABEL_CHOICES = (
        ('P', 'primary'),
        ('S', 'secondary'),
        ('D', 'danger')
    )

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)
    property_title =models.CharField( max_length=255)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(Lga,
                            on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    condition = models.CharField(max_length=25,choices=CONDITION, blank=True, null=True)
    property_offer = models.ForeignKey(Offer,on_delete=models.CASCADE, blank=True, null=True)
    property_price = models.DecimalField(decimal_places=0,
                                   max_digits=30)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True, blank=True)
    slug = models.SlugField(max_length=200,blank=True)
    property_area = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    building_age = models.CharField(max_length=25,choices=AGE , null=True, blank=True)
    rent_period = models.CharField(max_length=25,choices=PERIOD, null=True, blank=True)
    property_room = models.CharField(max_length=25,choices=ROOMS, null=True, blank=True)
    bedroom = models.CharField(max_length=25,choices=BEDROOMS, null=True, blank=True)
    bathroom = models.CharField(max_length=25,choices=BATHROOMS, null=True, blank=True)
    lot_size = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    plan_image = models.ImageField(upload_to='plans_images/',
                                   null=True, blank=True,default='profile/None/no-img.jpg')

    church = models.BooleanField(default=False, null=True, blank=True)
    school = models.BooleanField(default=False, null=True, blank=True)
    mosque = models.BooleanField(default=False, null=True, blank=True)
    market = models.BooleanField(default=False, null=True, blank=True)
    hospital = models.BooleanField(default=False, null=True, blank=True)
    resturant = models.BooleanField(default=False, null=True, blank=True)
    beach = models.BooleanField(default=False, null=True, blank=True)
    air_conditioning = models.BooleanField(default=False, null=True, blank=True)
    parking = models.BooleanField(default=False, null=True, blank=True)
    sewer = models.BooleanField(default=False, null=True, blank=True)
    water = models.BooleanField(default=False, null=True, blank=True)
    lawn = models.BooleanField(default=False, null=True, blank=True)
    swimming_pool = models.BooleanField(default=False, null=True, blank=True)
    barbecue = models.BooleanField(default=False, null=True, blank=True)
    tv_cable = models.BooleanField(default=False, null=True, blank=True)
    microwave = models.BooleanField(default=False, null=True, blank=True)
    wi_fi = models.BooleanField(default=False, null=True, blank=True)
    gym = models.BooleanField(default=False, null=True, blank=True)
    active = models.BooleanField(default=True)
    objects = AdsManager()#for active

    def __str__(self):
        return self.property_title

    def get_absolute_url(self):
        return reverse('home:ad_detail', args=[self.id, self.slug])

    def get_first_image(self):
        images = list(self.images.all())
        return images[0:3] if images else None

    def get_second_image(self):
        images = list(self.images.all())
        return images[0:1] if images else None

# def get_image_filename(instance, filename):
#     title = instance.ads.property_title
#     slug = slugify(title)
#     return "post_images/%s-%s" % (slug, filename)


class AdsImages(models.Model):
    ads = models.ForeignKey(Ads,related_name="images", on_delete=models.CASCADE)
    ad_image = models.ImageField(upload_to='ads/', default='profile/None/no-img.jpg', null=True, blank=True)

    def get_ordering_queryset(self):
        return self.ads.images.all()
