## crear una clase llamada vehicuilo capaz de prosesar la informacion basica de los mismo en una consecionaria. Debera tener constructor. Los atributos del vehiculo son:
## patente, marca, modelo, kilometraje. 
## Crear metodos (de acceso) getter y (modificacion) setter. Mostrar por pantalla y modificar el kilometraje.

class Vehiculo:
    def __init__ (self, patente, marca, modelo, kilometraje):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

  def get_patente(self):
        return self.patente

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_kilometraje(self):
        return self.kilometraje

    # Métodos Setter
    def set_kilometraje(self, nuevo_kilometraje):
        self.kilometraje = nuevo_kilometraje
