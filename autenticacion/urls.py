from django.urls import path

from .views import VistaRegistro, cerrar_session , logear

urlpatterns = [
    path("", VistaRegistro.as_view( ), name='Autenticacion'),
    path("cerrar_session", cerrar_session , name='Cerrar_session'),
    path("logear", logear , name='Logear'),
]

