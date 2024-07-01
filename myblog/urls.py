
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Blogapp.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('Membersapp/',include('membersapp.urls')), 
    path('tinymce/',include('tinymce.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
