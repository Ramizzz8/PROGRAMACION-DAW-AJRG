print("Lista de la compra v0.1")

listadelacompra = []

while True:
  print("Selecciona una opción:")
  print("1.- Añadir producto")
  print("2.- Ver lista de la compra")
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
  elif opcion == 2:
    print("Has seleccionado la opción de ver lista de la compra")
    for producto in listadelacompra:
      print("--------------------")
      print("Producto:", producto["nombre"])
      print("Cantidad:", producto["cantidad"])
      print("--------------------")

