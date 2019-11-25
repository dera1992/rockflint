from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('my_property/', views.my_property, name='my_property'),
    path('bookmarked/', views.bookmarked, name='bookmarked'),
    path('delete_post/(<pk>\d+)/', views.delete_post, name='delete_post'),
    path('hide_post/(<pk>\d+)/', views.hide_post, name='hide_post'),

]