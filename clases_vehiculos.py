class Vehiculo():
    def __init__(self, placa, marca, modelo, color, kilometraje, tipo_combustible):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = kilometraje
        self.tipo_combustible = tipo_combustible
                
class Carro(Vehiculo):
    def __init__(self, placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_pasajeros):
        super().__init__(placa, marca, modelo, color, kilometraje, tipo_combustible)
        self.capacidad_pasajeros = capacidad_pasajeros

class Motocicleta(Vehiculo):
    def __init__(self, placa, marca, modelo, color, kilometraje, tipo_combustible, cilindrada):
        super().__init__(placa, marca, modelo, color, kilometraje, tipo_combustible)
        self.cilindrada = cilindrada

class Camion(Vehiculo):
    def __init__(self, placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_carga):
        super().__init__(placa, marca, modelo, color, kilometraje, tipo_combustible)
        self.capacidad_carga = capacidad_carga
