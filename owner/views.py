# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from account.models import Profile
from advert.models import Ads, AdsImages, Category
from advert.forms import AdsForm
from django.db.models import Q
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import random

@login_required
def my_property(request):
    myab_list = Ads.objects.filter(profile__user=request.user)
    profile = Profile.objects.get(user=request.user)
    ads = Ads.objects.filter(active=True)
    lates = Ads.objects.all().order_by('-created_date')[:3]
    counts = Ads.objects.all().values('category__name').annotate(total=Count('category'))

    paginator = Paginator(myab_list, 6)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get('page')
    try:
        myab = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        myab = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        myab = paginator.page(paginator.num_pages)
    return render(request, 'owner/my_property.html', {'myab': myab, 'profile': profile, 'ads': ads, 'lates': lates,
                                                 'counts': counts, 'page_request_var': page_request_var})



def bookmarked(request):
    return render(request, 'owner/bookmarked.html', {})

@login_required
def delete_post(request,pk=None):
    ad = Ads.objects.get(id=pk)
    ad.is_active = False
    messages.success(request, "Successfuly deleted")
    return redirect('home:my_aids')
