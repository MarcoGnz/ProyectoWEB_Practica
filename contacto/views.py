from django.shortcuts import render
from .forms import FormularioContacto
# Create your views here.

def contacto(request):
    fomulario_contacto = FormularioContacto
    
    return render(request, 'contacto/contacto.html', {"miformulario" : fomulario_contacto })
