# Definimos la clase base 'Vehiculo'
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado

    # Método para obtener la marca del vehículo
    def get_marca(self):
        return self.__marca

    # Método para obtener el modelo del vehículo
    def get_modelo(self):
        return self.__modelo

    # Método que será sobrescrito en la clase derivada
    def tipo_vehiculo(self):
        raise NotImplementedError("Este método debe ser sobrescrito en la clase derivada")

# Definimos la clase derivada 'Automovil' que hereda de 'Vehiculo'
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamamos al constructor de la clase base
        self.__puertas = puertas  # Atributo privado

    # Método sobrescrito para especificar el tipo de vehículo
    def tipo_vehiculo(self):
        return "Automóvil"

    # Método para obtener el número de puertas del automóvil
    def get_puertas(self):
        return self.__puertas

# Definimos otra clase derivada 'Motocicleta' que hereda de 'Vehiculo'
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Llamamos al constructor de la clase base
        self.__tipo = tipo  # Atributo privado

    # Método sobrescrito para especificar el tipo de vehículo
    def tipo_vehiculo(self):
        return "Motocicleta"

    # Método para obtener el tipo de motocicleta
    def get_tipo(self):
        return self.__tipo

# Función para demostrar el polimorfismo
def mostrar_info_vehiculo(vehiculo):
    print(f"Vehículo: {vehiculo.get_marca()} {vehiculo.get_modelo()} - Tipo: {vehiculo.tipo_vehiculo()}")

# Creación de instancias de las clases
automovil = Automovil("Toyota", "Corolla", 4)
motocicleta = Motocicleta("Yamaha", "MT-07", "Deportiva")

# Demostración de la funcionalidad
mostrar_info_vehiculo(automovil)        # Salida: Vehículo: Toyota Corolla - Tipo: Automóvil
mostrar_info_vehiculo(motocicleta)      # Salida: Vehículo: Yamaha MT-07 - Tipo: Motocicleta

# Imprimir información adicional
print(f"El {automovil.get_marca()} {automovil.get_modelo()} tiene {automovil.get_puertas()} puertas.")
print(f"La {motocicleta.get_marca()} {motocicleta.get_modelo()} es de tipo {motocicleta.get_tipo()}.")

