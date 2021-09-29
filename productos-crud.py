##Archivo: productos-crud.py
# Autor: Saira Zapata
#Fecha: 16-9-2021
# Descripción: CRUD de productos, y uso de la libreria Tkinter.
# C Create/Crear
# R Read/Leer
# U Update/Actualizar
# D Delete/Eliminar
#-----------------
# Tecnologías
# Lenguaje de programción: Python
# Interfaz gráfica: Tkinder (librería que incorpora Python)
# Base de datos: SQL Lite, Base de datos relacional.


# Importamos la librería tkinter
from tkinter import ttk
from tkinter import *

# Importamos librería para conectar a la BD
import sqlite3

class Producto:
    # Inicialización
    def __init__(self, window):
        self.wind = window
        self.wind.title('Aplicación de productos')

        #Contenenor [Frame]
        frame = LabelFrame(self.wind, text = "Registra un nuevo producto")
        frame.grid(row = 0, column = 0, columnspan= 3, pady = 20)

        # Input Nombre
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Input Precio
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.precio = Entry(frame)
        self.precio.grid(row = 2, column = 1)

        # Boton para añadir producto
        ttk.Button(frame, text = "Guardar producto").grid(row = 3, columnspan = 2, sticky = W + E)

        # Tabla
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Precio', anchor = CENTER)

        # Botones con las acciones
        ttk.Button(text = "Editar producto").grid(row = 5, column = 0, sticky = W + E, pady = 10)
        ttk.Button(text = "Eliminar producto").grid(row = 5, column = 1, sticky = W + E, pady = 10)

        #Mock?
        # Filling the Rows
        self.get_products()

        # Get Products from Database
    def get_products(self):
        # Limpia la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Data de prueba
        db_rows = [{"nombre": "Maquina", "precio": "1299"},{"nombre": "Ordenador", "precio": "2269"},{"nombre": "Tablet", "precio": "736"}]
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row.get('nombre'), values = row.get('precio'))
    
#Ejecuta el contructor de la clase Producto
if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    window.mainloop();
