#CRUD
#Create
#Read
#Update
#Delete

print("Programa de gestion de clientes v0.1 Andres Julian Ramirez Guerrero")

#Muestro opciones en el menu para el usuario
print("Seleccione una opcion")
print("1-Instertar un cliente")
print("2-Listar clientes")
print("3-Actualizar clientes")
print("4-Eliminar clientes")

#Le permito escoger una opcion

opcion = input("Escoje una opcion: ")
opcion = int(opcion) #convierto a entero

#

while True: #Esto es un bucle infinito pero controlado usando break y elif
    if opcion == 1:
        print("Vamos a insertar a cliente")
        nuevocliente = input("Introduce el nombre de un cliente: ")
        clientes.append(nuevocliente)
        elif opcion2 == 2:
            print("Veremos los clientes")
        elif opcion3 == 3:
            print("Vamos a actualizar un cliente")
        elif opcion4 == 4:
            print("Vamos a eliminar un cliente")
        else:
            break
