import os
from clases_vehiculos import Carro, Motocicleta, Camion

class GestorVehiculos():
    def __init__(self):
        self.carros = 'carros.txt'
        self.motocicletas = 'motocicletas.txt'
        self.camiones = 'camiones.txt'
        
    def ingresar_vehiculo(self):
        tipo_vehiculo = input('Ingrese el tipo de vehículo a ingresar (carro, motocicleta, camión): ')
        if tipo_vehiculo == 'carro':
            placa = input('Ingrese la placa del carro: ')
            marca = input('Ingrese la marca del carro: ')
            modelo = input('Ingrese el modelo del carro: ')
            color = input('Ingrese el color del carro: ')
            kilometraje = input('Ingrese el kilometraje del carro: ')
            tipo_combustible = input('Ingrese el tipo de combustible del carro: ')
            capacidad_pasajeros = input('Ingrese la capacidad de pasajeros del carro: ')
            carro = Carro(placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_pasajeros)
            with open(self.carros, 'a') as archivo:
                archivo.write(f'{carro.placa},{carro.marca},{carro.modelo},{carro.color},{carro.kilometraje},{carro.tipo_combustible},{carro.capacidad_pasajeros}\n')
            print('Carro ingresado correctamente.')
        elif tipo_vehiculo == 'motocicleta':
            placa = input('Ingrese la placa de la motocicleta: ')
            marca = input('Ingrese la marca de la motocicleta: ')
            modelo = input('Ingrese el modelo de la motocicleta: ')
            color = input('Ingrese el color de la motocicleta: ')
            kilometraje = input('Ingrese el kilometraje de la motocicleta: ')
            tipo_combustible = input('Ingrese el tipo de combustible de la motocicleta: ')
            cilindrada = input('Ingrese la cilindrada de la motocicleta: ')
            motocicleta = Motocicleta(placa, marca, modelo, color, kilometraje, tipo_combustible, cilindrada)
            with open(self.motocicletas, 'a') as archivo:
                archivo.write(f'{motocicleta.placa},{motocicleta.marca},{motocicleta.modelo},{motocicleta.color},{motocicleta.kilometraje},{motocicleta.tipo_combustible},{motocicleta.cilindrada}\n')
            print('Motocicleta ingresada correctamente.')
        elif tipo_vehiculo == 'camión':
            placa = input('Ingrese la placa del camión: ')
            marca = input('Ingrese la marca del camión: ')
            modelo = input('Ingrese el modelo del camión: ')
            color = input('Ingrese el color del camión: ')
            kilometraje = input('Ingrese el kilometraje del camión: ')
            tipo_combustible = input('Ingrese el tipo de combustible del camión: ')
            capacidad_carga = input('Ingrese la capacidad de carga del camión: ')
            camion = Camion(placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_carga)
            with open(self.camiones, 'a') as archivo:
                archivo.write(f'{camion.placa},{camion.marca},{camion.modelo},{camion.color},{camion.kilometraje},{camion.tipo_combustible},{camion.capacidad_carga}\n')
            print('Camión ingresado correctamente.')
        
    def buscar_vehiculo(self):
        placa_buscar = input('Ingrese la placa del vehículo a buscar: ')
        tipo_vehiculo = input('Ingrese el tipo de vehículo a buscar (carro, motocicleta, camión): ')
        if tipo_vehiculo == 'carro':
            with open(self.carros, 'r') as archivo:
                for linea in archivo:
                    placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_pasajeros = linea.strip().split(',')
                    if placa == placa_buscar:
                        print(f'Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Color: {color}, Kilometraje: {kilometraje}, Tipo de combustible: {tipo_combustible}, Capacidad de pasajeros: {capacidad_pasajeros}')
                        break
                else:
                    print('Carro no encontrado.')
        elif tipo_vehiculo == 'motocicleta':
            with open(self.motocicletas, 'r') as archivo:
                for linea in archivo:
                    placa, marca, modelo, color, kilometraje, tipo_combustible, cilindrada = linea.strip().split(',')
                    if placa == placa_buscar:
                        print(f'Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Color: {color}, Kilometraje: {kilometraje}, Tipo de combustible: {tipo_combustible}, Cilindrada: {cilindrada}')
                        break
                else:
                    print('Motocicleta no encontrada.')
        elif tipo_vehiculo == 'camión':
            with open(self.camiones, 'r') as archivo:
                for linea in archivo:
                    placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_carga = linea.strip().split(',')
                    if placa == placa_buscar:
                        print(f'Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Color: {color}, Kilometraje: {kilometraje}, Tipo de combustible: {tipo_combustible} Capacidad de carga: {capacidad_carga}')
                        break
                else:
                    print('Camión no encontrado.')
    
    def modificar_vehiculo(self):
        placa_buscar = input('Ingrese la placa del vehículo a modificar: ')
        tipo_vehiculo = input('Ingrese el tipo de vehículo a modificar (carro, motocicleta, camión): ')
        vehiculos_actualizados = []
        if tipo_vehiculo == 'carro':
            with open(self.carros, 'r') as archivo:
                for linea in archivo:
                    placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_pasajeros = linea.strip().split(',')
                    if placa == placa_buscar:
                        color = input('Ingrese el nuevo color: ')
                        vehiculos_actualizados.append(f'{placa},{marca},{modelo},{color},{kilometraje},{tipo_combustible},{capacidad_pasajeros}\n')
                    else:
                        vehiculos_actualizados.append(linea)
            with open(self.carros, 'w') as archivo:
                for vehiculo in vehiculos_actualizados:
                    archivo.write(vehiculo)
            print('Carro modificado correctamente.')
        elif tipo_vehiculo == 'motocicleta':
            with open(self.motocicletas, 'r') as archivo:
                for linea in archivo:
                    placa, marca, modelo, color, kilometraje, tipo_combustible, cilindrada = linea.strip().split(',')
                    if placa == placa_buscar:
                        color = input('Ingrese el nuevo color: ')
                        vehiculos_actualizados.append(f'{placa},{marca},{modelo},{color},{kilometraje},{tipo_combustible},{cilindrada}\n')
                    else:
                        vehiculos_actualizados.append(linea)
            with open(self.motocicletas, 'w') as archivo:
                for vehiculo in vehiculos_actualizados:
                    archivo.write(vehiculo)
            print('Motocicleta modificada correctamente.')
        elif tipo_vehiculo == 'camión':
            with open(self.camiones, 'r') as archivo:
                for linea in archivo:
                    placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_carga = linea.strip().split(',')
                    if placa == placa_buscar:
                        color = input('Ingrese el nuevo color: ')
                        vehiculos_actualizados.append(f'{placa},{marca},{modelo},{color},{kilometraje},{tipo_combustible},{capacidad_carga}\n')
                    else:
                        vehiculos_actualizados.append(linea)
            with open(self.camiones, 'w') as archivo:
                for vehiculo in vehiculos_actualizados:
                    archivo.write(vehiculo)
            print('Camión modificado correctamente.')
            
    def mostrar_vehiculos(self):
        print('Carros:')
        with open(self.carros, 'r') as archivo:
            for linea in archivo:
                placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_pasajeros = linea.strip().split(',')
                print(f'Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Color: {color}, Kilometraje: {kilometraje}, Tipo de combustible: {tipo_combustible}, Capacidad de pasajeros: {capacidad_pasajeros}')
        print('Motocicletas:')
        with open(self.motocicletas, 'r') as archivo:
            for linea in archivo:
                placa, marca, modelo, color, kilometraje, tipo_combustible, cilindrada = linea.strip().split(',')
                print(f'Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Color: {color}, Kilometraje: {kilometraje}, Tipo de combustible: {tipo_combustible}, Cilindrada: {cilindrada}')
        print('Camiones:')
        with open(self.camiones, 'r') as archivo:
            for linea in archivo:
                placa, marca, modelo, color, kilometraje, tipo_combustible, capacidad_carga = linea.strip().split(',')
                print(f'Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Color: {color}, Kilometraje: {kilometraje}, Tipo de combustible: {tipo_combustible}, Capacidad de carga: {capacidad_carga}')