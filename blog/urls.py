from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/', views.blog_detail, name='edit_post'),
    path('blog/', views.post_list, name='list'),
    path('create/', views.post_create, name='post_create'),
    path('<slug>[\w-]+/', views.post_detail, name='detail'),
    path('<slug>[\w-]+/edit/', views.post_update, name='update'),
    path('<slug>[\w-]+/delete/', views.post_delete, name='post_delete'),
    path('blog/create_contact/', views.create_contact, name='create_contact')
]