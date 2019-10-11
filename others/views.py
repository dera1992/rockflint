# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import  HttpResponse
import json
from django.core import serializers
import ast
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
def agent_list(request):
    return render(request,'others/agent_list.html', {})


def agent_detail(request):
    return render(request, 'others/agent_detail.html', {})

def agency_list(request):
    return render(request, 'others/agency_list.html', {})


def agency_detail(request):
    return render(request, 'others/agency_detail.html', {})