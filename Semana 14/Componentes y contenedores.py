import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Lista para almacenar eventos
        self.eventos = []

        # Crear contenedores (Frames)
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        # Componentes de la lista de eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Componentes de entrada de datos
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Selector de hora (12 horas con AM/PM)
        tk.Label(self.frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.horas = [str(i).zfill(2) for i in range(1, 13)]  # Horas de 1 a 12
        self.hora_combobox = ttk.Combobox(self.frame_entrada, values=self.horas, width=3)
        self.hora_combobox.grid(row=0, column=3, padx=5, pady=5)
        self.hora_combobox.set("12")  # Valor predeterminado

        tk.Label(self.frame_entrada, text=":").grid(row=0, column=4, padx=0, pady=5)
        self.minutos = [str(i).zfill(2) for i in range(60)]  # Minutos de 00 a 59
        self.minuto_combobox = ttk.Combobox(self.frame_entrada, values=self.minutos, width=3)
        self.minuto_combobox.grid(row=0, column=5, padx=5, pady=5)
        self.minuto_combobox.set("00")  # Valor predeterminado

        self.periodos = ['AM', 'PM']  # Períodos AM/PM
        self.periodo_combobox = ttk.Combobox(self.frame_entrada, values=self.periodos, width=3)
        self.periodo_combobox.grid(row=0, column=6, padx=5, pady=5)
        self.periodo_combobox.set("AM")  # Valor predeterminado

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=0, column=7, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(self.frame_entrada, width=30)
        self.descripcion_entry.grid(row=0, column=8, padx=5, pady=5)

        # Botones
        self.agregar_btn = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_btn.pack(side=tk.LEFT, padx=5)

        self.eliminar_btn = tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento)
        self.eliminar_btn.pack(side=tk.LEFT, padx=5)

        self.salir_btn = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.salir_btn.pack(side=tk.LEFT, padx=5)

    def agregar_evento(self):
        """Agrega un evento a la lista."""
        fecha = self.fecha_entry.get()
        hora = self.hora_combobox.get()
        minuto = self.minuto_combobox.get()
        periodo = self.periodo_combobox.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and minuto and periodo and descripcion:
            hora_completa = f"{hora}:{minuto} {periodo}"
            self.eventos.append((fecha, hora_completa, descripcion))
            self.tree.insert("", tk.END, values=(fecha, hora_completa, descripcion))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        """Elimina el evento seleccionado de la lista."""
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este evento?")
            if confirmacion:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Nada seleccionado", "Por favor, seleccione un evento para eliminar.")

    def limpiar_campos(self):
        """Limpia los campos de entrada."""
        # No intentes establecer una fecha vacía en el DateEntry
        self.hora_combobox.set("12")
        self.minuto_combobox.set("00")
        self.periodo_combobox.set("AM")
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()