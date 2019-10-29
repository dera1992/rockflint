# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from advert.models import Ads, AdsImages, Category, State ,Offer,Lga
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
from account.models import Profile
from .forms import MessageForm, ScheduleForm
from django.core.mail import send_mail



def home_list(request, category_slug=None):
    category = None
    ads = Ads.objects.filter(active=True).order_by("?")[:6]
    latests = Ads.objects.filter(active=True).order_by('-created', '?')[:6]
    qs = Ads.objects.all()
    categories = Category.objects.all()
    states = State.objects.all()
    cities = Lga.objects.all()
    offers = Offer.objects.all()
    # adsimage = AdsImages.objects.filter(ads=ad)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        ads = ads.filter(category=category)
    return render(request,'home/index.html', {'category': category,'categories': categories,'ads': ads,'latests':latests,
                                              'queryset': qs,'states':states,'cities':cities,'offers':offers})


def ad_detail(request, id, slug):
    ad = get_object_or_404(Ads,
                                id=id,
                                slug=slug,
                                active=True)
    adsimage = AdsImages.objects.filter(ads=ad)
    ad_similar = Ads.objects.filter(category=ad.category).exclude(id=ad.id).order_by('?')[:7]
    same_city = Ads.objects.filter(city=ad.city).exclude(id=ad.id).order_by('?')[:7]
    latests = Ads.objects.filter(active=True).order_by('-created', '?')[:6]
    profile = Profile.objects.get(user=ad.profile.user)
    receiver = [profile.user.email]
    if request.POST:
        form = MessageForm(request.POST)
        schedule_form =ScheduleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(ad.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['phone'], cd['email'], ad.property_title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(ad.property_title, post_url, cd['phone'],
                                                                    cd['comments'])
            sender = cd['email']
            to = receiver
            send_mail(subject, message, sender, to)
            messages.add_message(request, messages.INFO, 'Your message has been sent')
            form = MessageForm()
        else:
            if schedule_form.is_valid():
                cd = schedule_form.cleaned_data
                post_url = request.build_absolute_uri(ad.get_absolute_url())
                subject = '{} ({}) recommends you reading "{}"'.format(cd['phone'], cd['email'], ad.property_title)
                message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(ad.property_title, post_url, cd['phone'],
                                                                        cd['comments'])
                sender = cd['email']
                to = receiver
                send_mail(subject, message, sender, to)
                messages.add_message(request, messages.INFO, 'Your message has been sent')
                form = ScheduleForm()


    else:
        form = MessageForm()
        schedule_form = ScheduleForm()
    return render(request, 'home/detail.html', {'ad':ad,'adsimage':adsimage, 'ad_similar':ad_similar,
                                               'profile':profile,'form': form,'same_city':same_city,'latests':latests,
                                                'schedule_form':schedule_form})

def delete_post(request,pk=None):
    ad = Ads.objects.get(id=pk)
    ad.delete()
    messages.success(request, "Successfuly deleted")
    return redirect('home:my_aids')


def category_count(request):
    counts = Ads.objects.all().values('category__name').annotate(total=Count('category'))
    lates = Ads.objects.order_by('-created_date')[:3]
    return render(request, 'home/footer.html', {'counts': counts, 'lates':lates})


def send_message(request,ad_id):
    ad = get_object_or_404(Ads, id=ad_id)
    sent = False

    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(ad.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], ad.property_title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(ad.property_title, post_url, cd['phone'], cd['comments'])
            sender = cd['email']
            to = ad.profile.user.email
            send_mail(subject, message,sender,to)
            sent = True

            messages.add_message(request, messages.SUCCESS, 'Your message has been sent')

    else:
        form = MessageForm()

        args = {'form': form,'sent': sent}
        return render(request, 'home/detail.html', args)