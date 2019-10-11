# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Ads, AdsImages, Category, SubCategory,Lga
from .forms import AdsImageForm, AdsForm

from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def postAd(request):

    ImageFormSet = modelformset_factory(AdsImages,
                                        form=AdsImageForm, extra=7)
    if request.method == 'POST':

        postForm = AdsForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=AdsImages.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    ad_image = form['ad_image']
                    photo = AdsImages(post=post_form, ad_image=ad_image)
                    photo.save()
            messages.success(request,
                             "Your property has been created")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = AdsForm()
        formset = ImageFormSet(queryset=AdsImages.objects.none())
    return render(request, 'advert/post.html',
                  {'postForm': postForm, 'formset': formset})


def editAd(request, id):
    if id:
        ad = Ads.objects.get(pk=id)  # if this is an edit form, replace the author instance with the existing one
    else:
        ad= Ads()
    postForm = AdsForm(instance=ad) # setup a form for the parent

    ImageFormSet = inlineformset_factory(Ads, AdsImages, fields=('ad_title',),extra=0, can_delete=True)
    formset = ImageFormSet(instance=ad)

    if request.method == "POST":
        postForm = AdsForm(request.POST)

        if id:
            postForm = AdsForm(request.POST, instance=ad)

        formset = ImageFormSet(request.POST, request.FILES)

        if postForm.is_valid():
            created_ad = postForm.save(commit=False)
            formset = ImageFormSet(request.POST, request.FILES, instance=created_ad)

            if formset.is_valid():
                created_ad.save()
                for form in formset.cleaned_data:
                    if form:
                        ad_image = form['ad_image']
                        photo = AdsImages(post=postForm, ad_image=ad_image)
                        photo.save()
                messages.success(request,
                                 "Error updating your form")
                formset.save()
                return HttpResponseRedirect(created_ad.get_absolute_url())

    return render("advert/edit_post.html", {
        "postForm": postForm,
        "formset": formset,
    })

def load_cities(request):
    state_id = request.GET.get('state')
    cities = Lga.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'advert/city_dropdown_list_options.html', {'cities': cities})



