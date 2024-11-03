from django.urls import path

from . import views

urlpatterns = [
    path("", views.auntenticacion, name='Autenticacion'),
]

