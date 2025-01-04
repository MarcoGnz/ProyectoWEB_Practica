from django.contrib import admin

from .models import Pedido, LineaPedido

    
admin.site.register([Pedido, LineaPedido])  # Register the models
  


