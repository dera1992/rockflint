from django.urls import path
from . import views

app_name = 'others'

urlpatterns = [
    path('agent_list/', views.agent_list, name='agent_list'),
    path('agent_detail/<id>/', views.agent_detail, name='agent_detail'),
    path('agency_list/', views.agency_list, name='blog_list'),
    path('agency_detail/<id>/', views.agency_detail, name='agency_detail'),
    path('create_contact/', views.create_contact, name='create_contact')
]