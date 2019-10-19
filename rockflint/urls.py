from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('advert/',include('advert.urls', namespace='advert')),
    path('blog/',include('blog.urls', namespace='blog')),
    path('',include('home.urls', namespace='home')),
    path('others/',include('others.urls', namespace='others')),
    path('owner/',include('owner.urls', namespace='owner')),
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
