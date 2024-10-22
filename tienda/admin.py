from django.contrib import admin

# Register your models here.
from .models import CategoriaProductos, Producto
# Register your models here.

class CategoriaProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(CategoriaProductos, CategoriaProductosAdmin)
admin.site.register(Producto, ProductosAdmin)