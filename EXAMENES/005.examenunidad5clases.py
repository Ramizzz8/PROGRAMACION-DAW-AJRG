#Programa clase clientes
#v0.1 Andres Julian Ramirez Guerrrero
# Este programa es una mini-aplicacion CRUD que hace gestiona clientes
import pickle
import os

class Cliente():
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

# Crear lista vacía de clientes
clientes = []

# Intentar cargar clientes previamente guardados
try:
    if os.path.exists('clientes.pkl'):
        with open('clientes.pkl', 'rb') as f:
            clientes = pickle.load(f)
except Exception as e:
    print("Error al cargar los clientes:", e)

# Ofrecer menú de dos opciones: crear cliente o listar clientes
print("########## PROGRAMA GESTIÓN DE CLIENTES v0.1 ##########")
print("---------- ########### BIENVENIDO ########### ----------")

while True:
    print("Escoge una opción: ")
    print("1.- Insertar un cliente")
    print("2.- Listar clientes")
    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        nombre = input("¿Cuál es el nombre del cliente?: ")
        apellido = input("¿Cuáles son los apellidos del cliente?: ")
        email = input("¿Cuál es el email del cliente?: ")
        telefono = int(input("¿Cuál es el teléfono del cliente?: "))
        clientes.append(Cliente(nombre, apellido, email, telefono))

        # Guardar la lista de clientes cada vez que se crea uno
        with open('clientes.pkl', 'wb') as f:
            pickle.dump(clientes, f)

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("\nEste es el cliente con ID:", identificador)
            print("Nombre:", cliente.nombre)
            print("Apellido:", cliente.apellido)
            print("Email:", cliente.email)
            print("Teléfono:", cliente.telefono)
            identificador += 1





