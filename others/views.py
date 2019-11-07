# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from account.models import Profile
from django.shortcuts import get_object_or_404
from advert.models import Ads, AdsImages, Category, State ,Offer,Lga
from django.db.models import Count
from django.http import  HttpResponse

from django.contrib import messages
from .forms import InformationForm
from django.core.mail import send_mail
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def agent_list(request):
    agent_list = Profile.objects.filter(agent_type="2",active=True)
    query = request.GET.get('q')
    if query:
        agent_list = agent_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone=query) |
            Q(description__icontains=query)|
            Q(address__icontains=query)
        )
    paginator = Paginator(agent_list, 6)
    page_request_var = "page"
    page = request.GET.get('page')
    try:
        agents = paginator.page(page)
    except PageNotAnInteger:
        agents = paginator.page(1)
    except EmptyPage:
        agents = paginator.page(paginator.num_pages)
    return render(request,'others/agent_list.html', {'agents':agents})


def agent_detail(request,id):
    agent = get_object_or_404(Profile,
                             id=id,
                             active=True)
    agent_ads = Ads.objects.filter(profile=agent).order_by('?')[:10]
    latests = Ads.objects.filter(active=True).order_by('-created', '?')[:6]
    qs = Ads.objects.all()
    categories = Category.objects.all()
    states = State.objects.all()
    cities = Lga.objects.all()
    offers = Offer.objects.all()
    return render(request, 'others/agent_detail.html', {'agent':agent,'agent_ads':agent_ads,'latests':latests,'categories': categories,
                                              'queryset': qs,'states':states,'cities':cities,'offers':offers,})

def agency_list(request):
    agentes_list = Profile.objects.filter(agent_type="3",active=True)
    query = request.GET.get('q')
    if query:
        agentes_list = agentes_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone=query) |
            Q(description__icontains=query) |
            Q(address__icontains=query)
        )
    paginator = Paginator(agentes_list, 6)
    page_request_var = "page"
    page = request.GET.get('page')
    try:
        agentes = paginator.page(page)
    except PageNotAnInteger:
        agentes = paginator.page(1)
    except EmptyPage:
        agentes = paginator.page(paginator.num_pages)
    return render(request, 'others/agency_list.html', {'agentes':agentes})


def agency_detail(request,id):
    agency = get_object_or_404(Profile,
                             id=id,
                             active=True)
    agency_ads = Ads.objects.filter(profile=agency).order_by('?')[:10]
    latests = Ads.objects.filter(active=True).order_by('-created', '?')[:6]
    qs = Ads.objects.all()
    categories = Category.objects.all()
    states = State.objects.all()
    cities = Lga.objects.all()
    offers = Offer.objects.all()
    return render(request, 'others/agency_detail.html', {'agency':agency,'agency_ads':agency_ads,'latests':latests,'categories': categories,
                                              'queryset': qs,'states':states,'cities':cities,'offers':offers,})

def create_contact(request):
    if request.POST:
        form = InformationForm(request.POST)
        if form.is_valid():
            post_info = form.save(commit=False)
            # post.user = request.user
            post = form.cleaned_data
            subject = post['subject']
            message ='Hello "{}" sent you a message below \n{}'.format( post['name'], post['message'])
            sender = post['email']
            to = ['ezechdr16@gmail.com']
            send_mail(subject, message, sender, to)
            post_info.save()

            # text = form.cleaned_data['headline','content']
            messages.add_message(request, messages.SUCCESS, 'Your message has been recieved')
            form = InformationForm()
            return redirect('others:create_contact')

    else:
        form = InformationForm()

        args = {'form': form}
        return render(request, 'others/contact.html', args)