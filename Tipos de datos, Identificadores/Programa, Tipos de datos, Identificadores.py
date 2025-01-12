# Programa para calcular el área de un círculo o un rectángulo.
# El usuario puede elegir la figura y proporcionar las dimensiones necesarias.

import math


def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * (radio ** 2)
    return area


def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    area = base * altura
    return area


def main():
    """Función principal que gestiona la interacción con el usuario."""
    continuar = True  # Variable booleana para controlar el bucle

    while continuar:
        print("Seleccione la figura para calcular el área:")
        print("1. Círculo")
        print("2. Rectángulo")
        opcion = input("Ingrese 1 o 2: ")

        if opcion == '1':
            # Calcular área del círculo
            radio_str = input("Ingrese el radio del círculo: ")
            radio = float(radio_str)  # Convertir a float
            area_circulo = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area_circulo:.2f}")

        elif opcion == '2':
            # Calcular área del rectángulo
            base_str = input("Ingrese la base del rectángulo: ")
            altura_str = input("Ingrese la altura del rectángulo: ")
            base = float(base_str)  # Convertir a float
            altura = float(altura_str)  # Convertir a float
            area_rectangulo = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area_rectangulo:.2f}")

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

        # Preguntar al usuario si desea continuar
        respuesta = input("¿Desea calcular otra área? (si/no): ").strip().lower()
        continuar = respuesta == 'si'  # Actualizar la variable booleana


if __name__ == "__main__":
    main()
