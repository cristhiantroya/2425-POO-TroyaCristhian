def obtener_temperaturas():
    """Función para obtener las temperaturas diarias de la semana."""
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas


def calcular_promedio(temperaturas):
    """Función para calcular el promedio de una lista de temperaturas."""
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)


def main():
    """Función principal que coordina la ejecución del programa."""
    print("Bienvenido al programa de promedio semanal del clima.")
    temperaturas = obtener_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print(f"\nLas temperaturas ingresadas son: {temperaturas}")
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()
d