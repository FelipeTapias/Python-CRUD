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

    #Nombre de la base de datos
    db_nombre = 'database.db'

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
        ttk.Button(frame, text = "Guardar producto", command= self.agregar_producto).grid(row = 3, columnspan = 2, sticky = W + E)

        # Mensaje de salida
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Tabla
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Precio', anchor = CENTER)

        # Botones con las acciones
        ttk.Button(text = "Editar producto").grid(row = 5, column = 0, sticky = W + E, pady = 10)
        ttk.Button(text = "Eliminar producto", command = self.eliminar_producto).grid(row = 5, column = 1, sticky = W + E, pady = 10)

        # Rellenar la tabla
        self.obtener_productos()
    
    #Metodo que ejecuta la consulta
    def run_query(self, query, parametros = ()):
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parametros)
            conn.commit()
        return resultado

    # Obtiene los productos de la base de datos
    def obtener_productos(self):
        # Limpia la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Consulta: Obtiene los datos
        query = 'SELECT * FROM producto ORDER BY precio DESC'
        db_rows = self.run_query(query)
        # Rellena los datos
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    # User Input Validation
    def validacion(self):
        return len(self.name.get()) != 0 and len(self.precio.get()) != 0
    
    def agregar_producto(self):
        if self.validacion():
            query = 'INSERT INTO producto VALUES(NULL, ?, ?)'
            parameters =  (self.name.get(), self.precio.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Producto {} ha sido agregado éxitosamente'.format(self.name.get())
            self.message['fg'] = 'green'
            self.name.delete(0, END)
            self.precio.delete(0, END)
        else:
            self.message['text'] = 'Campos requeridos'
            self.message['fg'] = 'red'
        self.obtener_productos()

    def eliminar_producto(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor selecciona un producto'
            self.message['fg'] = 'red'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM producto WHERE nombre = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Producto {} eliminado éxitosamente'.format(name)
        self.message['fg'] = 'green'
        self.obtener_productos()


#Ejecuta el contructor de la clase Producto
if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    window.mainloop();
