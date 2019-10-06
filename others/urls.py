from django.urls import path
from . import views

app_name = 'others'

urlpatterns = [
    path('agent_list/', views.agent_list, name='agent_list'),
    path('agent_detail/', views.agent_detail, name='agent_post'),
    path('agency_list/', views.agency_list, name='blog_list'),
    path('agency_detail/', views.agency_detail, name='edit_post'),
]