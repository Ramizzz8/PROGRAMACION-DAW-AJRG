'''
    Aplicacion de gestion de productos
    v0.1 Andres Julian Ramirez Guerrero
    Esta apliacion gestiona productos

'''

#Esta apliacion no tiene librerias para importar

#Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

#Creamos las variables globales
productos = []

#Primero le lanzamos un mensaje de bienvenida

print("Programa Gestor de Productos v0.1 (c) AJRG")

#Le mostramos al usuario las opciones que tiene

print("Seleccione una opcion: ")
print("1- Crear un nuevo producto")
print("2- Listar productos ")
print("3- Actualizar productos")
print("4- Vamos a eliminar productos")

#En funcion de la opcion que coja el usuaio
    #o bien creamos un nuevo producto
    #o bien listamos los productos
    #o bien actualizamos los productos
    #o bien eliminamos los productos
