import tkinter as tk
from tkinter import ttk, messagebox, font


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Fuente personalizada
        self.custom_font = font.Font(family="Helvetica", size=10)
        self.custom_font_bold = font.Font(family="Helvetica", size=10, weight="bold")

        # Variables
        self.tasks = []

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de tarea
        ttk.Label(main_frame, text="Nueva Tarea:", font=self.custom_font_bold).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 5))

        self.task_entry = ttk.Entry(main_frame, width=40, font=self.custom_font)
        self.task_entry.grid(row=1, column=0, padx=(0, 5), sticky=tk.EW)
        self.task_entry.focus()
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        # Botón Añadir
        add_btn = ttk.Button(main_frame, text="Añadir", command=self.add_task)
        add_btn.grid(row=1, column=1, sticky=tk.EW)

        # Lista de tareas
        self.task_list = tk.Listbox(
            main_frame,
            height=15,
            selectmode=tk.SINGLE,
            font=self.custom_font,
            activestyle="none",
            relief=tk.FLAT,
            highlightthickness=0
        )
        self.task_list.grid(row=2, column=0, columnspan=2, pady=(10, 5), sticky=tk.NSEW)
        self.task_list.bind("<Double-Button-1>", lambda e: self.toggle_task_completion())

        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.task_list.yview)
        scrollbar.grid(row=2, column=2, sticky=tk.NS)
        self.task_list.config(yscrollcommand=scrollbar.set)

        # Frame de botones inferiores
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, columnspan=3, pady=(10, 0), sticky=tk.EW)

        # Botones de acción
        complete_btn = ttk.Button(
            btn_frame,
            text="Marcar como Completada",
            command=self.toggle_task_completion
        )
        complete_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        delete_btn = ttk.Button(
            btn_frame,
            text="Eliminar Tarea",
            command=self.delete_task
        )
        delete_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        clear_btn = ttk.Button(
            btn_frame,
            text="Limpiar Todo",
            command=self.clear_all_tasks
        )
        clear_btn.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Configurar pesos de filas y columnas
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def toggle_task_completion(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

    def clear_all_tasks(self):
        if self.tasks:
            if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar todas las tareas?"):
                self.tasks = []
                self.update_task_list()
        else:
            messagebox.showinfo("Información", "No hay tareas para limpiar.")

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["text"]
            if task["completed"]:
                self.task_list.insert(tk.END, f"✓ {task_text}")
                self.task_list.itemconfig(tk.END, {'fg': 'gray'})
            else:
                self.task_list.insert(tk.END, f"○ {task_text}")
                self.task_list.itemconfig(tk.END, {'fg': 'black'})

#fin
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()