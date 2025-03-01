import pickle

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado correctamente.")
        else:
            print("Error: El ID del producto no existe.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: El ID del producto no existe.")

    def buscar_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.get_nombre() == nombre]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)
        print("Inventario guardado correctamente.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Error: El archivo no existe.")

# Interfaz de Usuario
def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Guardar Inventario")
    print("7. Cargar Inventario")
    print("8. Salir")

def main():
    inventario = Inventario()
    archivo = "inventario.dat"

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_inventario(archivo)

        elif opcion == "7":
            inventario.cargar_inventario(archivo)

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()