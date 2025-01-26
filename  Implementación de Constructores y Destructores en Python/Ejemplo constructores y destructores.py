class ReservaHotel:
    def __init__(self, nombre_cliente, fecha_reserva):
        """
        Constructor de la clase ReservaHotel.
        Inicializa los atributos de la reserva y simula la creación de una entrada en la base de datos.
        :param nombre_cliente: Nombre del cliente que realiza la reserva.
        :param fecha_reserva: Fecha en la que se realiza la reserva.
        """
        self.nombre_cliente = nombre_cliente
        self.fecha_reserva = fecha_reserva
        self.id_reserva = self.crear_reserva()
        print(
            f"Reserva creada para {self.nombre_cliente} en la fecha {self.fecha_reserva}. ID Reserva: {self.id_reserva}")

    def crear_reserva(self):
        """
        Simula la creación de una reserva en una base de datos.
        Genera un ID único para la reserva.
        :return: ID de la reserva.
        """
        # Aquí podríamos tener lógica para generar un ID único, por simplicidad usamos un número fijo
        return hash((self.nombre_cliente, self.fecha_reserva))

    def cancelar_reserva(self):
        """
        Simula la cancelación de una reserva.
        Aquí podríamos incluir lógica para eliminar la reserva de una base de datos.
        """
        print(f"Reserva con ID {self.id_reserva} ha sido cancelada para {self.nombre_cliente}.")

    def __del__(self):
        """
        Destructor de la clase ReservaHotel.
        Simula la limpieza de recursos al eliminar una reserva.
        """
        print(f"Liberando recursos para la reserva con ID {self.id_reserva}.")


# Ejemplo de uso de la clase ReservaHotel
if __name__ == "__main__":
    # Crear una nueva reserva
    reserva1 = ReservaHotel("Cristhian Jimenez ", "2025-02-15")

    # Cancelar la reserva
    reserva1.cancelar_reserva()

    # La instancia se eliminará automáticamente al salir del bloque if
