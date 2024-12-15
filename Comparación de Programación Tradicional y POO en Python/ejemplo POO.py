class DiaClima:
    """Clase que representa el clima de un día específico."""

    def __init__(self, temperatura):
        self._temperatura = temperatura  # Atributo privado

    @property
    def temperatura(self):
        """Método para acceder a la temperatura."""
        return self._temperatura


class SemanaClima:
    """Clase que representa una semana de clima."""

    def __init__(self):
        self.dias = []  # Lista para almacenar los días de clima

    def agregar_dia(self, temperatura):
        """Método para agregar un día con su temperatura."""
        dia = DiaClima(temperatura)
        self.dias.append(dia)

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas de la semana."""
        if not self.dias:
            return 0
        total_temperaturas = sum(dia.temperatura for dia in self.dias)
        return total_temperaturas / len(self.dias)


def main():
    """Función principal que coordina la ejecución del programa."""
    print("Bienvenido al programa de promedio semanal del clima.")
    semana = SemanaClima()

    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                semana.agregar_dia(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    promedio = semana.calcular_promedio()

    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()

