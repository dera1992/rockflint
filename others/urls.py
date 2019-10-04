from django.urls import path
from . import views

app_name = 'others'

urlpatterns = [
    path('blog_list/', views.agent_list, name='blog_list'),
    path('blog_detail/', views.agent_detail, name='edit_post'),
    path('agency_list/', views.agency_list, name='blog_list'),
    path('agency_detail/', views.agency_detail, name='edit_post'),
]