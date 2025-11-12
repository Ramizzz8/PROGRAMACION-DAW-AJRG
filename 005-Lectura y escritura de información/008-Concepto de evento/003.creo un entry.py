import tkinter as tk

ventana = tk.Tk()

marco= tk.Frame(ventana)

#DNI / NIE
tk.Label(marco,text="Introduce el DNI/NIE del cliente: ")
dninie= tk.Entry(marco)
dninie.pack(padx=10,pady=10)
#Nombre
tk.Label(marco,text="Introduce el nombre del cliente: ")
nombre= tk.Entry(marco)
nombre.pack(padx=10,pady=10)
#Apellidos
tk.Label(marco,text="Introduce los apellidos del cliente: ")
apellidos= tk.Entry(marco)
apellidos.pack(padx=10,pady=10)
#Email
tk.Label(marco,text="Introduce el email del cliente: ")
email= tk.Entry(marco)
email.pack(padx=10,pady=10)