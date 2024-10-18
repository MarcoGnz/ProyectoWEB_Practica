from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):
    
    return render(request, 'ProyectoWEBapp/home.html')

def tienda(request):
    
    return render(request, 'ProyectoWEBapp/tienda.html')


def contacto(request):
    
    return render(request, 'ProyectoWEBapp/contacto.html')