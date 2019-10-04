# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def my_property(request):
        return render(request,'owner/my_property.html', {})


def bookmarked(request):
    return render(request, 'owner/bookmarked.html', {})
