from django.urls import path
from . import views

app_name = 'others'

urlpatterns = [
    path('allagent_list/', views.allagent_list, name='allagent_list'),
    path('agent_list/', views.agent_list, name='agent_list'),
    path('agent_detail/<id>/', views.agent_detail, name='agent_detail'),
    path('agent_detail_rating/<id>/', views.agent_detail_rating, name='agent_detail_rating'),
    path('agency_list/', views.agency_list, name='agency_list'),
    path('agency_detail/<id>/', views.agency_detail, name='agency_detail'),
    path('agency_detail_rating/<id>/', views.agency_detail_rating, name='agency_detail_rating'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('testimonies/', views.testimonies, name='testimonies'),
    path('about_us/', views.about_us, name='about_us'),
]