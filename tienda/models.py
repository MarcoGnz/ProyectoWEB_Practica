from django.db import models
from django.utils import timezone  # Importar el módulo timezone


# Modelo para la Categoría de Productos
class CategoriaProductos(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción de la categoría")
    created = models.DateTimeField(default=timezone.now)  # Fecha de creación automática
    updated = models.DateTimeField(auto_now=True)      # Fecha de última actualización automática

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# Modelo para Productos
class Producto(models.Model):
    categoria = models.ForeignKey(CategoriaProductos, on_delete=models.CASCADE, related_name="productos", verbose_name="Categoría")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Cantidad en stock")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True, verbose_name="Imagen del producto")
    created = models.DateTimeField(default=timezone.now)  # Fecha de creación automática
    updated = models.DateTimeField(auto_now=True)      # Fecha de última actualización automática

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
