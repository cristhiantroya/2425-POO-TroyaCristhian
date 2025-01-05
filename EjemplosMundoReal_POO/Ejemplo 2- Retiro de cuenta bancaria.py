class CuentaBancaria:
    """Clase que representa una cuenta bancaria."""

    def __init__(self, titular, saldo_inicial=0):
        """Inicializa la cuenta con el nombre del titular y un saldo inicial."""
        self.titular = titular
        self.saldo = saldo_inicial

    def retirar(self, cantidad):
        """Realiza un retiro de la cuenta si hay suficiente saldo."""
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad}. Saldo actual: ${self.saldo}.")
            return True
        else:
            print(f"Error: Saldo insuficiente para retirar ${cantidad}. Saldo actual: ${self.saldo}.")
            return False

    def depositar(self, cantidad):
        """Realiza un depósito en la cuenta."""
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso: ${cantidad}. Saldo actual: ${self.saldo}.")
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")

    def mostrar_saldo(self):
        """Muestra el saldo actual de la cuenta."""
        print(f"Saldo actual de {self.titular}: ${self.saldo}")

    def __str__(self):
        """Devuelve una representación en cadena de la cuenta bancaria."""
        return f"Cuenta de {self.titular} - Saldo: ${self.saldo}"


# Ejemplo de uso del sistema de cuentas bancarias

# Crear una cuenta bancaria
cuenta1 = CuentaBancaria("Cristhian Troya", 5000)

# Mostrar información inicial de la cuenta
print(cuenta1)

# Realizar algunos depósitos
cuenta1.depositar(200)  # Depósito exitoso
cuenta1.depositar(-50)  # Error en el depósito

# Realizar algunos retiros
cuenta1.retirar(100)  # Retiro exitoso
cuenta1.retirar(700)  # Error por saldo insuficiente

# Mostrar saldo final
cuenta1.mostrar_saldo()
