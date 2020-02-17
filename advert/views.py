# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ads, AdsImages, Category,Lga
from .forms import AdsImageForm, AdsForm, AdsEditImageForm, AdsEditForm

from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def postAd(request):

    ImageFormSet = modelformset_factory(AdsImages,
                                        form=AdsImageForm, extra=9)
    if request.method == 'POST':

        postForm = AdsForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=AdsImages.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.profile = request.user.profile
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    ad_image = form['ad_image']
                    photo = AdsImages(ads=post_form, ad_image=ad_image)
                    photo.save()
                    messages.success(request,"Your property has been created succcessfully")
            return redirect('owner:my_property')
        else:
            messages.error(request, 'Sorry,Error creating your property')
            print(postForm.errors, formset.errors)
    else:
        postForm = AdsForm()
        formset = ImageFormSet(queryset=AdsImages.objects.none())
    return render(request, 'advert/post.html',
                  {'postForm': postForm, 'formset': formset})

@login_required
def editAd(request, pk):
    ad = Ads.objects.get(id=pk)
    ImageFormSet = modelformset_factory(AdsImages,fields=('ad_image',), extra=9, max_num=9)
    if ad.profile.user != request.user:
        raise Http404()
    if request.method == 'POST':

        postForm = AdsEditForm(request.POST, request.FILES, instance=ad)
        formset = ImageFormSet(request.POST, request.FILES,request.FILES or None)

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.profile = request.user.profile
            post_form.save()

            data = AdsImages.objects.filter(ads=ad)
            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        photo = AdsImages(ads=ad, ad_image=f.cleaned_data.get('ad_image'))
                        photo.save()
                    elif f.cleaned_data['ad_image'] is False:
                        photo = AdsImages.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()
                    else:
                        photo = AdsImages(ads=ad, ad_image=f.cleaned_data.get('ad_image'))
                        d = AdsImages.objects.get(id=data[index].id)
                        d.image = photo.ad_image
                        d.save()
            messages.success(request, "{} has been successfully updated!".format(ad.property_title))
            return redirect('owner:my_property')
        else:
            messages.error(request, 'Sorry,Error updating your property')
            print(postForm.errors, formset.errors)
    else:
        postForm = AdsEditForm(instance=ad)
        formset = ImageFormSet(queryset=AdsImages.objects.filter(ads=ad))
    return render(request, 'advert/post.html',
                  {'postForm': postForm, 'formset': formset})


# def editAd(request, pk):
#     ad = Ads.objects.get(id=pk)
#     ImageFormSet = inlineformset_factory(Ads, AdsImages, fields=('ad_image',),extra=4, max_num=4,
#                                         min_num=4)
#
#     if request.method == "POST":
#         postForm = AdsEditForm(request.POST or None, request.FILES or None, instance=ad)
#         formset = ImageFormSet(request.POST or None, request.FILES or None)
#
#         if postForm.is_valid():
#             post_form = postForm.save(commit=False)
#             formset = ImageFormSet(request.POST, request.FILES, instance=post_form)
#
#             if formset.is_valid():
#                 post_form.save()
#                 for form in formset.cleaned_data:
#                     if form:
#                         ad_image = form['ad_image']
#                         photo = AdsImages(ads=post_form, ad_image=ad_image)
#                         photo.save()
#                         messages.success(request,"You have successfully updated your form")
#                     else:
#                         messages.error(request, 'Error updating your form')
#                 formset.save()
#                 return HttpResponseRedirect("/")
#     else:
#         postForm = AdsEditForm(instance=ad)
#         formset = ImageFormSet(instance=ad,queryset=AdsImages.objects.filter(ads_id=ad.id))
#     return render(request,'advert/edit_post.html',{'postForm': postForm,
#         'formset': formset,
#     })

#
# def editAd(request, pk):
#     if id:
#         ad = Ads.objects.get(id=pk)  # if this is an edit form, replace the author instance with the existing one
#     else:
#         ad= Ads()
#     postForm = AdsEditForm(instance=ad) # setup a form for the parent
#
#     ImageFormSet = inlineformset_factory(Ads, AdsImages, fields=('ad_image',),extra=1)
#     formset = ImageFormSet(instance=ad)
#
#     if request.method == "POST":
#         postForm = AdsEditForm(request.POST, request.FILES)
#
#         if id:
#             postForm = AdsEditForm(request.POST, instance=ad)
#
#         formset = ImageFormSet(request.POST, request.FILES)
#
#         if postForm.is_valid():
#             post_form = postForm.save(commit=False)
#             formset = ImageFormSet(request.POST, request.FILES, instance=post_form)
#
#             if formset.is_valid():
#                 post_form.save()
#                 for form in formset.cleaned_data:
#                     if form:
#                         ad_image = form['ad_image']
#                         photo = AdsImages(ads=post_form, ad_image=ad_image)
#                         photo.save()
#                         messages.success(request,"You have successfully updated your form")
#                     else:
#                         messages.error(request, 'Error updating your form')
#                 formset.save()
#                 return HttpResponseRedirect("/")
#
#     return render(request,'advert/edit_post.html',{'postForm': postForm,
#         'formset': formset,
#     })



def load_cities(request):
    state_id = request.GET.get('state')
    cities = Lga.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'advert/city_dropdown_list_options.html', {'cities': cities})



