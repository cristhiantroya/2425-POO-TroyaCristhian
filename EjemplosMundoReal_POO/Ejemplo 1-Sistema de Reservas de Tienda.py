class Producto:
    """Clase que representa un producto en la tienda."""

    def __init__(self, nombre, precio, stock):
        """Inicializa el producto con su nombre, precio y cantidad en stock."""
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reservar(self, cantidad):
        """Reserva una cantidad del producto si hay suficiente stock."""
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"{self.nombre} - Precio: ${self.precio}, Stock: {self.stock}"


class Reserva:
    """Clase que representa una reserva de productos."""

    def __init__(self):
        """Inicializa una reserva vacía."""
        self.productos_reservados = {}

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la reserva si se puede reservar."""
        if producto.reservar(cantidad):
            self.productos_reservados[producto.nombre] = cantidad
            print(f"Reservado {cantidad} unidades de {producto.nombre}.")
        else:
            print(f"No hay suficiente stock para reservar {cantidad} unidades de {producto.nombre}.")

    def mostrar_reserva(self):
        """Muestra los productos reservados y sus cantidades."""
        print("Productos reservados:")
        for nombre, cantidad in self.productos_reservados.items():
            print(f"{nombre}: {cantidad} unidades")


# Ejemplo de uso del sistema de reservas

# Creación de algunos productos
producto1 = Producto("Laptop", 1200, 5)
producto2 = Producto("Teléfono", 800, 10)
producto3 = Producto("Auriculares", 150, 0)

# Mostrar información inicial de los productos
print(producto1)
print(producto2)
print(producto3)

# Crear una reserva
reserva = Reserva()

# Agregar productos a la reserva
reserva.agregar_producto(producto1, 2)  # Reserva exitosa
reserva.agregar_producto(producto2, 3)  # Reserva exitosa
reserva.agregar_producto(producto3, 1)  # No hay suficiente stock

# Mostrar productos reservados
reserva.mostrar_reserva()

# Mostrar información actualizada de los productos después de las reservas
print("\nInformación actualizada de los productos:")
print(producto1)
print(producto2)
print(producto3)
