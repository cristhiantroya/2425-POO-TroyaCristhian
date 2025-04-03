import tkinter as tk
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Lista para almacenar las tareas
        self.tasks = []

        # Crear y configurar los widgets
        self.create_widgets()

        # Configurar atajos de teclado
        self.setup_keyboard_shortcuts()

    def create_widgets(self):
        # Etiqueta y campo de entrada para añadir nuevas tareas
        self.task_entry_label = tk.Label(self.root, text="Nueva tarea:")
        self.task_entry_label.pack(pady=(10, 0))

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=(0, 10))
        self.task_entry.focus_set()  # El cursor comienza en el campo de entrada

        # Botones para añadir, marcar como completada y eliminar tareas
        self.add_button = tk.Button(self.root, text="Añadir", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=(20, 5))

        self.complete_button = tk.Button(self.root, text="Completar", command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.root, text="Eliminar", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=(5, 20))

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=(10, 10))

        # Scrollbar para la lista de tareas
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

    def setup_keyboard_shortcuts(self):
        # Atajo para añadir tarea (Enter)
        self.root.bind("<Return>", lambda event: self.add_task())
        # Atajo para marcar tarea como completada (C)
        self.root.bind("c", lambda event: self.mark_completed())
        # Atajo para eliminar tarea (Delete o D)
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("d", lambda event: self.delete_task())
        # Atajo para cerrar la aplicación (Escape)
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["completed"]:
                text = f"[COMPLETADA] {text}"
            self.task_listbox.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()