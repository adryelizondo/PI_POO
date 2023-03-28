from tkinter import *
from tkinter import ttk
import tkinter as tk

from controladorBD import *

controlador = controladorBD()

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())

ventana = Tk()
ventana.title("CRUD usuarios")
ventana.geometry("600x400")

panel = ttk.Notebook(ventana)
panel.pack(fill= "both", expand = "yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

titulo = Label(pestana1, text = "Registro de Usuarios", fg = "blue", font = ("Modern", 18)).pack()

varNom = tk.StringVar()
lblNom = Label(pestana1, text = "Username: ").pack()
txtNom = Entry(pestana1, textvariable = varNom).pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text = "Email: ").pack()
txtCor = Entry(pestana1, textvariable = varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text = "Password: ").pack()
txtCon = Entry(pestana1, textvariable = varCon, show = "*").pack()

btnGuardar = Button(pestana1, text = "Guardar Usuario", command = ejecutaInsert).pack()

panel.add(pestana1, text = "Formulario de usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")

ventana.mainloop()