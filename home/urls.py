from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_list, name='home'),
    path('<int:id>/<slug:slug>/', views.ad_detail, name='ad_detail'),
    path('<slug:category_slug>/', views.home_list, name='ads_list_by_category'),
    path('delete_post/(<pk>\d+)/', views.delete_post, name='delete_post'),
    path('category_count/',views.category_count,name='category_count'),

]