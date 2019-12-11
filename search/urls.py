from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'search'

urlpatterns = [
    path('filter/',views.filter,name='filter'),
#    path('ajax_filter/',views.ajax_filter,name='ajax_filter'),

]