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
def home_list(request):
        return render(request,'home/index.html', {})


def ad_detail(request):
    return render(request, 'home/detail.html', {})