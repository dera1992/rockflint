from django.urls import path
from . import views

app_name = 'advert'

urlpatterns = [
    path('post/', views.postAd, name='post'),
    path('edit_post/', views.editAd, name='edit_post'),
]