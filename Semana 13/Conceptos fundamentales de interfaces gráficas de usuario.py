import tkinter as tk
from tkinter import messagebox

def agregar_info():
    info = entry.get()
    if info:
        listbox.insert(tk.END, info)
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

def limpiar_info():
    entry.delete(0, tk.END)  # Limpiar el campo de texto
    listbox.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Información")

# Crear componentes
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

entry = tk.Entry(ventana, width=50)
entry.pack(pady=10)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_info)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()





