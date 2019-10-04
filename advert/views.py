# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Ads, AdsImages, Category, Condition, Location, SubCategory
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import  HttpResponse
import json
from django.core import serializers
import ast
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
def postAd(request):
        return render(request,'advert/post.html', {})


def editAd(request):
    return render(request, 'advert/edit_post.html', {})




