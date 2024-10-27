from django.shortcuts import render, redirect

from .carro import  Carro

from tienda.models  import Producto

# Create your views here.

def agragar_producto(request, prodcuto_id):
  carro = Carro(request)
  producto = Producto.objects.get(id=prodcuto_id)
  carro.agregar(producto=producto)
  
  return redirect("tienda")

def eliminar_producto(request, prodcuto_id):
  carro = Carro(request)
  producto = Producto.objects.get(id=prodcuto_id)
  carro.eliminar(producto=producto)
  
  return redirect("tienda")

def restar_producto(request, prodcuto_id):
  carro = Carro(request)
  producto = Producto.objects.get(id=prodcuto_id)
  carro.restar_producto(producto=producto)
  
  return redirect("tienda")

def limpiar_carro(request, prodcuto_id):
  carro = Carro(request)
  carro.limpiar_carro()
  
  return redirect("tienda")
