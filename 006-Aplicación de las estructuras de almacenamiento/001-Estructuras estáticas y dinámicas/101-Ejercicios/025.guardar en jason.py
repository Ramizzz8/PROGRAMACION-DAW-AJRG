print("Lista de la compra v0.1")
import json #importamos la librería json para trabajar con ficheros json

listadelacompra = []

while True:
  print("Selecciona una opción:")
  print("1.- Añadir producto")
  print("2.- Ver lista de la compra")
  print("3.- Salir")
  opcion = int(input("Opción: "))

  if opcion == 1:
    print("Has seleccionado la opción de añadir producto")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    listadelacompra.append(
      {
        "nombre": nombre,
        "cantidad": cantidad
      }
    )
    archivo = open("listadelacompra.json", "w")#abro el archivo en modo escritura
    json.dump(listadelacompra, archivo)#guardo la lista en el archivo json
    archivo.close()#cierro el archivo
  elif opcion == 2:
    print("Has seleccionado la opción de ver lista de la compra")
    for producto in listadelacompra:
      print("--------------------")
      print("Producto:", producto["nombre"])
      print("Cantidad:", producto["cantidad"])
      print("--------------------")
  elif opcion == 3:
    print("Saliendo del programa...")
    break

