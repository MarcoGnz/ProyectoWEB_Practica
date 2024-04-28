from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return HttpResponse("Inicio de pagina")

def servicios(request):
    
    return HttpResponse("pagina  servicios")

def tienda(request):
    
    return HttpResponse("pagina de tienda")

def blog(request):
    
    return HttpResponse("blog")

def contacto(request):
    
    return HttpResponse("contacto")