from django.urls import path
from . import views

app_name = 'advert'

urlpatterns = [
    path('edit_post/(<pk>\d+)/', views.editAd, name='edit_post'),
    path('post/', views.postAd, name='post'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here
]
