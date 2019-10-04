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
def blog_list(request):
        return render(request,'blog/blog_list.html', {})


def blog_detail(request):
    return render(request, 'blog/blog_detail.html', {})