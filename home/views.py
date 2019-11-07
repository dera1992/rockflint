# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from advert.models import Ads, AdsImages, Category, State ,Offer,Lga
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404,HttpResponse
from django.urls import reverse
import json
from django.core import serializers
import ast
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from account.models import Profile
from .forms import MessageForm, ScheduleForm
from django.core.mail import send_mail
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required



def home_list(request, category_slug=None):
    category = None
    ads = Ads.objects.filter(active=True).order_by("?")[:6]
    latests = Ads.objects.filter(active=True).order_by('-created', '?')[:6]
    qs = Ads.objects.all()
    categories = Category.objects.all()
    states = State.objects.all()
    cities = Lga.objects.all()
    offers = Offer.objects.all()
    agents = Profile.objects.filter(agent_type="2", active=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        ads = ads.filter(category=category)
    return render(request,'home/index.html', {'category': category,'categories': categories,'ads': ads,'latests':latests,
                                              'queryset': qs,'states':states,'cities':cities,'offers':offers,'agents':agents})


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
    is_favourite = False

    if ad.favourite.filter(id=request.user.id).exists():
        is_favourite = True

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
                                                'schedule_form':schedule_form,'is_favourite': is_favourite,})
@login_required
def ads_favourite_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts': favourite_posts,
    }
    return render(request, 'owner/bookmarked.html', context)

@login_required
def favourite_ads(request, id):
    ad = get_object_or_404(Ads, id=id)
    print(ad)
    if ad.favourite.filter(id=request.user.id).exists():
        ad.favourite.remove(request.user)
    else:
        ad.favourite.add(request.user)
    return HttpResponseRedirect(ad.get_absolute_url())

@login_required
def delete_post(request,pk=None):
    ad = Ads.objects.get(id=pk)
    if request.user != ad.profile.user:
        raise Http404()
    ad.delete()
    messages.success(request, "You property has been successfuly deleted")
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