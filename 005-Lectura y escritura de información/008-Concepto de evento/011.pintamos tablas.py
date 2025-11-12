import tkinter as tk
from tkinter import ttk
import mysql.connector

conexion = mysql.connector.connect(
  host="local.host",
  user ="empresadam",
  password="Empresadam123$",
  database = "empresadam"
) 
cursor = conexion.cursor()
ventana = tk.Tk()
arbol = ttk.Treeview(ventana, columns = ("dninie","nombre","apellidos","email"),show = "headings")
arbol.heading("dninie", text ="DNI/NIE del cliente")
arbol.heading("nombre", text ="Nombre del cliente")
arbol.heading("apellidos", text = "Apellidos del cliente")
arbol.heading("email", text = "Email del cliente")

arbol.insert("", "end",values =("Andres Julian", "Ramirez"))
arbol.insert("", "end",values =("Olek", "Bodgantroika"))

arbol.pack(padx=20,pady=20)

ventana.mainloop()
