from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    path(r'^$', views.home_list, name='home'),
    path('ad_detail/', views.ad_detail, name='ad_detail'),
]