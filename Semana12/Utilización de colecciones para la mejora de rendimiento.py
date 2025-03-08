import json
import msvcrt

class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, isbn):
        self.libros_prestados.append(isbn)

    def devolver_libro(self, isbn):
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)

class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()
        self.usuarios = []

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        if libro and not libro.prestado:
            libro.prestado = True
            self.guardar_libros()
            usuario = self.encontrar_usuario(id_usuario)
            if usuario:
                usuario.prestar_libro(isbn)
            else:
                print("Usuario no encontrado.")
            print(f"Libro {isbn} prestado con éxito.")
        else:
            print("Libro no disponible para préstamo.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        if libro and libro.prestado:
            libro.prestado = False
            self.guardar_libros()
            usuario = self.encontrar_usuario(id_usuario)
            if usuario:
                usuario.devolver_libro(isbn)
            else:
                print("Usuario no encontrado.")
            print(f"Libro {isbn} devuelto con éxito.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

    def registrar_usuario(self, nombre, id_usuario):
        if not self.encontrar_usuario(id_usuario):
            nuevo_usuario = Usuario(nombre, id_usuario)
            self.usuarios.append(nuevo_usuario)
            print(f"Usuario {nombre} registrado con ID {id_usuario}.")
        else:
            print("ID de usuario ya existente.")

    def encontrar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def mostrar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print(f"ID: {usuario.id_usuario}, Nombre: {usuario.nombre}")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Mostrar Libros\n3. Prestar Libro\n4. Devolver Libro\n5. Registrar Usuario\n6. Mostrar Usuarios\n7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
            input("Presiona Enter para continuar...")
        elif opcion == '2':
            biblioteca.mostrar_libros()
            input("Presiona Enter para continuar...")
        elif opcion == '3':
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID de usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
            input("Presiona Enter para continuar...")
        elif opcion == '4':
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID de usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
            input("Presiona Enter para continuar...")
        elif opcion == '5':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID de usuario: ")
            biblioteca.registrar_usuario(nombre, id_usuario)
            input("Presiona Enter para continuar...")
        elif opcion == '6':
            biblioteca.mostrar_usuarios()
            input("Presiona Enter para continuar...")
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()