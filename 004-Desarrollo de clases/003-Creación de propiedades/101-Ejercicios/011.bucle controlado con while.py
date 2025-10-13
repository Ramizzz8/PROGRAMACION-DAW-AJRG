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

while True:

    print("Seleccione una opcion: ")
    print("1- Crear un nuevo producto")
    print("2- Listar productos ")
    print("3- Actualizar productos")
    print("4- Vamos a eliminar productos")

    #En funcion de la opcion que coja el usuaio
    opcion = int(input("Escoge tu opcion: "))

    #IF / ELIF

        #o bien creamos un nuevo producto
    if opcion == 1:
        print("Creamos un nuevo producto")
        producto1 = producto()      #creo una nueva instancia en la clase
        pruducto1.nombre = input("Introduce el nombre del producto: ")       
        
        #escribo la propiedad
        producto1.precio = int(input("Cual es el precio del producto: "))    #escribo la propiedad

        #o bien listamos los productos
    elif opcion == 2:
        print("Vamos a listar los productos")
        #o bien actualizamos los productos
    elif opcion == 3:
        print("Vamos a actualizar un producto")
        #o bien eliminamos los productos
    elif opcion == 4:
        print("Eliminemos un producto")
    else:
        print("Introduce una opcion valida")


