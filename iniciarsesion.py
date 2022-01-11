from tkinter import *
from functools import *
from typing import Type
from conexion import Conexion



class iniciarSesion(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.iniciarComponentes()
        self.bd = Conexion()

    def validarSesion(self, usuario, password):
        nombre_usuario = usuario.get()
        contraseña_usuario = password.get()
        print(f"Usuario ingresado: {nombre_usuario}")
        print(f"Contraseña ingresada: {contraseña_usuario}")
        resultado = self.bd.validarCredenciales(nombre_usuario, contraseña_usuario)
        if(len(resultado)>0):
            print("Validado.")
       

        
    def iniciarComponentes(self):
        usuariosLabel = Label(self,text="Usuario").grid(row=0, column=0)
        usuario = StringVar()
        entradaUsuario = Entry(self, textvariable=usuario).grid(row=0, column=1)

        passwLabel = Label(self,text="Contraseña").grid(row=1, column=0)
        password = StringVar()
        entradaUsuario = Entry(self, textvariable=password,  show = '*').grid(row=1, column=1)

        validarSesion = partial(self.validarSesion, usuario, password) 

        login = Button(self, text="Iniciar Sesion",
         command=validarSesion,
          bg="white",
          fg = "black").grid(row = 4, column=0)
          

ventana = Tk()
ventana.geometry("400x300")
ventana.title("ventana de inicio de sesion")
aplicacion = iniciarSesion(master=ventana)

aplicacion.mainloop()

    


