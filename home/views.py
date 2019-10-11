# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from advert.models import Ads, AdsImages, Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import  HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from django.core import serializers
import ast
# Create your views here.
from django.views.decorators.csrf import csrf_exempt



def home_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    ads = Ads.objects.filter(active=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        ads = ads.filter(category=category)
    return render(request,'home/index.html', {'category': category,
                                              'categories': categories,'ads': ads})


def ad_detail(request, id, slug):
    ad = get_object_or_404(Ads,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'home/detail.html', {'ad':ad})

def delete_post(request,pk=None):
    ad = Ads.objects.get(id=pk)
    ad.delete()
    messages.success(request, "Successfuly deleted")
    return redirect('home:my_aids')


def category_count(request):
    counts = Ads.objects.all().values('category__name').annotate(total=Count('category'))
    lates = Ads.objects.order_by('-created_date')[:3]
    return render(request, 'home/footer.html', {'counts': counts, 'lates':lates})