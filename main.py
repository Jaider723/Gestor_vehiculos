from gestor import GestorVehiculos 

def miles_to_kilometers(miles):
    return miles * 1.60934

def main():
    archivo = GestorVehiculos()
    while True:
        print("\n--- Bienvenido al gestor de vehículos ---")
        print("1. Ingreso de nuevo vehículo")
        print("2. Buscar vehículo")
        print("3. Calcular millas a kilómetros")
        print("4. Modificar vehículo")
        print("5. Mostrar todos los vehículos")
        print("0. Salir")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            archivo.ingresar_vehiculo()
        elif opcion == '2':
            archivo.buscar_vehiculo()
        elif opcion == '3':
            miles = float(input("Ingrese las millas: "))
            print(f"{miles} millas son {miles_to_kilometers(miles)} kilómetros.")
        elif opcion == '4':
            archivo.modificar_vehiculo()
        elif opcion == '5':
            archivo.mostrar_vehiculos()
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()