from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/', views.blog_detail, name='edit_post'),
]