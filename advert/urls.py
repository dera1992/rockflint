from django.urls import path
from . import views

app_name = 'advert'

urlpatterns = [
    path('post/', views.postAd, name='post'),
    path('edit_post/', views.editAd, name='edit_post'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here
]
