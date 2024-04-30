from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request, 'ProyectoWEBapp/home.html')

def servicios(request):
    
    return render(request, 'ProyectoWEBapp/servicios.html')

def tienda(request):
    
    return render(request, 'ProyectoWEBapp/tienda.html')

def blog(request):
    
    return render(request, 'ProyectoWEBapp/blog.html')

def contacto(request):
    
    return render(request, 'ProyectoWEBapp/contacto.html')