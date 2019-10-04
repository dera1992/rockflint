from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('my_property/', views.my_property, name='my_property'),
    path('bookmarked/', views.bookmarked, name='bookmarked'),

]