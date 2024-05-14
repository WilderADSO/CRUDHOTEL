import tkinter as tk
from tkinter import ttk

class HotelCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Habitaciones - Hotel TRADICIONES")
        self.root.configure(bg="black")  # Configurar color de fondo negro

        # Nombres y tipos de habitaciones
        self.habitaciones = {
            "Lempira": "Sencilla",
            "Caturra": "Doble",
            "Casiopea": "Múltiple",
            "Pajarito": "Sencilla",
            "Batian": "Doble",
            "Marsellesa": "Múltiple",
            "Geisha": "Sencilla"
        }

        # Estado de ocupación de las habitaciones
        self.habitaciones_ocupadas = {habitacion: False for habitacion in self.habitaciones}

        # Crear variables de control para los campos de entrada
        self.nombre_var = tk.StringVar()
        self.tipo_var = tk.StringVar()
        self.ocupada_var = tk.BooleanVar()

        # Crear la interfaz de usuario
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y menú desplegable para seleccionar habitación
        ttk.Label(self.root, text="Habitación:", foreground="green", background="black", font=('Helvetica', 12)).grid(row=0, column=0, padx=5, pady=5)
        self.habitacion_combobox = ttk.Combobox(self.root, values=list(self.habitaciones.keys()), textvariable=self.nombre_var, state="readonly", font=('Helvetica', 12))
        self.habitacion_combobox.grid(row=0, column=1, padx=5, pady=5)

        # Etiquetas y campos de entrada
        ttk.Label(self.root, text="Tipo:", foreground="blue", background="black", font=('Helvetica', 12)).grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.tipo_var, state="readonly", font=('Helvetica', 12)).grid(row=1, column=1, padx=5, pady=5)

        # Checkbutton con estilo personalizado
        self.ocupada_checkbutton = ttk.Checkbutton(self.root, text="Ocupada", variable=self.ocupada_var, style='Accent.TCheckbutton', command=self.actualizar_disponibilidad)
        self.ocupada_checkbutton.grid(row=2, column=1, padx=5, pady=5)

        # Botones con colores personalizados
        ttk.Style().configure('Accent.TButton', foreground='black', background='blue')
        ttk.Button(self.root, text="Agregar", command=self.agregar_habitacion, style='Accent.TButton').grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(self.root, text="Buscar", command=self.buscar_habitacion, style='Accent.TButton').grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(self.root, text="Actualizar", command=self.actualizar_estado, style='Accent.TButton').grid(row=3, column=2, padx=5, pady=5)
        ttk.Button(self.root, text="Eliminar", command=self.eliminar_habitacion, style='Accent.TButton').grid(row=3, column=3, padx=5, pady=5)
        
        # Botones adicionales
        ttk.Button(self.root, text="Cargar Datos", command=self.cargar_datos, style='Accent.TButton').grid(row=4, column=0, padx=5, pady=5)
        ttk.Button(self.root, text="Limpiar Tabla", command=self.limpiar_tabla, style='Accent.TButton').grid(row=4, column=1, padx=5, pady=5)

        # Etiqueta para mostrar la cantidad de habitaciones disponibles por tipo
        self.disponibles_label = ttk.Label(self.root, text="", foreground="white", background="black", font=('Helvetica', 12))
        self.disponibles_label.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    def agregar_habitacion(self):
        nombre = self.nombre_var.get()
        tipo = self.tipo_var.get()
        ocupada = self.ocupada_var.get()

        # Aquí puedes agregar la lógica para agregar una habitación a la base de datos

        print("Habitación agregada:", nombre, tipo, "(Ocupada)" if ocupada else "(Disponible)")

    def buscar_habitacion(self):
        nombre = self.nombre_var.get()

        # Aquí puedes agregar la lógica para buscar una habitación en la base de datos
        # y mostrar la información en los campos de entrada

        tipo = self.habitaciones.get(nombre, "")
        self.tipo_var.set(tipo)

        print("Buscando habitación:", nombre)

    def actualizar_estado(self):
        nombre = self.nombre_var.get()
        ocupada = self.ocupada_var.get()

        # Actualizamos el estado de ocupación de la habitación seleccionada
        self.habitaciones_ocupadas[nombre] = ocupada

        # Aquí puedes agregar la lógica para actualizar el estado de una habitación
        # en la base de datos

        print("Actualizando estado de habitación:", nombre, "a", "Ocupada" if ocupada else "Disponible")

        # Actualizamos la disponibilidad de las habitaciones
        self.actualizar_disponibilidad()

    def eliminar_habitacion(self):
        nombre = self.nombre_var.get()

        # Aquí puedes agregar la lógica para eliminar una habitación de la base de datos

        print("Eliminando habitación:", nombre)

    def cargar_datos(self):
        # Aquí puedes agregar la lógica para cargar los datos desde la base de datos
        # Actualizamos la cantidad de habitaciones disponibles por tipo
        self.actualizar_habitaciones_disponibles()
        print("Cargando datos...")

    def limpiar_tabla(self):
        # Aquí puedes agregar la lógica para limpiar la tabla
        print("Limpiando tabla...")

    def actualizar_habitaciones_disponibles(self):
        # Reiniciamos los contadores
        disponibles_por_tipo = {tipo: 0 for tipo in set(self.habitaciones.values())}
        
        # Contamos las habitaciones disponibles por tipo
        for habitacion, ocupada in self.habitaciones_ocupadas.items():
            tipo = self.habitaciones[habitacion]
            if not ocupada:
                disponibles_por_tipo[tipo] += 1
        
        # Actualizamos la etiqueta
        disponibles_text = "Habitaciones disponibles:\n"
        for tipo, cantidad in disponibles_por_tipo.items():
            disponibles_text += f"{tipo}: {cantidad}\n"
        self.disponibles_label.config(text=disponibles_text)

    def actualizar_disponibilidad(self):
        # Actualizamos la disponibilidad cuando cambia el estado de ocupación
        self.actualizar_habitaciones_disponibles()

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelCRUDApp(root)
    root.mainloop()