from django.urls import path

from ProyectoWEBapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name= 'home'),
    
    path("sample", views.sample, name='Sample'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
