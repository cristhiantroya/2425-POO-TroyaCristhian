import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Tecnicas de Programacion/Ejemplo Tecnicas de Programacion.py',
        '2': 'Comparación de Programación Tradicional y POO en Python/ejemplo POO.py',
        '3': 'Comparación de Programación Tradicional y POO en Python/ejemplo programacion tradicional.py',
        '4': 'EjemplosMundoReal_POO/Ejemplo 1-Sistema de Reservas de Tienda.py',
        '5': 'EjemplosMundoReal_POO/Ejemplo 2- Retiro de cuenta bancaria.py',
        '6': 'Tipos de datos, Identificadores/Programa, Tipos de datos, Identificadores.py',
        '7': 'Clases, objetos, herencia, encapsulamiento y polimorfismo/Programa semana 6.py',
        '8': 'Implementación de Constructores y Destructores en Python/Ejemplo constructores y destructores.py',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()