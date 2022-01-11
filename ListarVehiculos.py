from tkinter import ttk
from tkinter import *
from functools import *
from conexion import *


class ListarVehiculos:
    def __init__(self, ventana):
        super().__init__()
        self.ventana=ventana
        self.ventana.title('listado de vehiculos')
        self.bd = Conexion()
        self.iniciarComponentes()

    def ingresarVehiculo(self, datosVehiculo):
        self.bd.crearVehiculo(datosVehiculo)
        self.obtenerElementos()

    def obtenerElementos(self):
        listadoVehiculos = self.bd.listaVehiculos()
        self.tree.delete(*self.tree.get_children())

        item = self.tree.insert("", END, text="Vehiculos")

        for row in listadoVehiculos:
            self.tree.insert(item, 'end', text=row[1], values=(row[3]))

    def iniciarComponentes(self):
        frame = LabelFrame(self.ventana,text="listar vehiculo")
        frame.grid(row=0, column=0, columnspan=3, pady=30)

        Label(frame, text="Marca").grid(row=1, column=0)
        self.marca = Entry(frame)
        self.marca.grid(row=1, column=1) 

        Label(frame, text="ID").grid(row=1, column=2)
        self.id = Entry(frame)
        self.id.grid(row=1, column=3) 

        Label(frame, text="Modelo").grid(row=2, column=0)
        self.modelo = Entry(frame)
        self.modelo.grid(row=2, column=1)

        ingresarVehiculo = partial(self.ingresarVehiculo, self.marca, self.id, self.modelo)

        Button(frame, text="Ingresar",
            command= ingresarVehiculo,
            bg = "white",
            fg = "black").grid(row=6, columnspan=2, sticky= W+E)

        self.tree = ttk.Treeview(height=10, columns=('#0','#1','#2'))
        self.tree.grid(row=7, column=0, columnspan=2)
        self.tree.heading('#0', text='Marca',anchor=CENTER)
        self.tree.heading('#1', text='ID',anchor=CENTER)
        self.tree.heading('#2', text='Modelo',anchor=CENTER)

        self.obtenerElementos()


if __name__ == "__main__":
    ventana = Tk()
    aplicacion = ListarVehiculos(ventana)
    ventana.mainloop()


        
       
         


