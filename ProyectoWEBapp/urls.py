from django.urls import path

from ProyectoWEBapp import views

urlpatterns = [
    path("", views.home, name= 'home'),
    path("servicios", views.servicios, name='Servicios'),
    path("tienda", views.tienda, name='Tienda'),
    path("blog", views.blog, name='Blog'),
    path("conectato", views.contacto, name='Contacto'),
]
