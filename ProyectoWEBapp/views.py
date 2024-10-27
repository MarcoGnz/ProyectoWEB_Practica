from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):
    
    return render(request, 'ProyectoWEBapp/home.html')

def sample(request):
    return render(request, "ProyectoWEBapp/sample.html")


