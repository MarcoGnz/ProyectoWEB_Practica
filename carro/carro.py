class Carro:
  def __init__(self, request):
    self.request =  request
    self.session = request.session
    carro = self.session.get("carro")
    if not carro:
      carro =  self.session["carro"] = {}
    #else:
    self.carro = carro
      
  def agregar(self, producto):
    if  str(producto.id) not in self.carro.keys():
      self.carro[producto.id] = {
        'producto_id':producto.id,
        'nombre' : producto.nombre,
        'precio': f"{producto.precio:.2f}",  # Formato con dos decimales        
        'cantidad' : 1,
        'imagen' : producto.imagen.url
      }
    else:
      for  key, value in self.carro.items():
        if key == str(producto.id):
          self.carro[key]['cantidad'] += 1
          value['precio'] = f"{round(float(value['precio']) + float(producto.precio), 2):.2f}"  # Actualiza y limita a dos decimales
          break
    self.guardar_carro()
    
  def guardar_carro(self):
    self.session["carro"] = self.carro
    self.session.modified = True
    
  def eliminar(self,  producto):
    producto.id = str(producto.id)
    if  producto.id in self.carro:
      del self.carro[producto.id]
      self.guardar_carro()
      
  def restar_producto(self, producto):
    for  key, value in self.carro.items():
        if key == str(producto.id):
          self.carro[key]['cantidad'] -= 1
          value['precio'] = f"{round(float(value['precio']) - float(producto.precio), 2):.2f}"  # Resta y limita a dos decimales
          if  self.carro[key]['cantidad'] < 1:
            self.eliminar(producto)
          break
    self.guardar_carro()
    
  def  limpiar_carro(self):
    self.session["carro"] = {}
    self.session.modified = True
