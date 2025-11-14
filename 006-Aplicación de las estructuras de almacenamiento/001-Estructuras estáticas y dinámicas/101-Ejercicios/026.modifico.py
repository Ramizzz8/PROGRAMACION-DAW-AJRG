print("Programa para vendedores en linea v0.1")
print("Gestiona los productos que tienes en venta")

import json #importamos la librería json para trabajar con ficheros json

productosenventa = []

while True:
  print("Selecciona una opción:")
  print("1.- Añadir producto")
  print("2.- Ver mi tienda")
  print("3.- Salir")
  opcion = int(input("Opción: "))

  if opcion == 1:
    print("Has seleccionado la opción de añadir producto")
    categoria = input("Categoría del producto: ")
    marca = input("Marca del producto: ")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio del producto: "))
    productosenventa.append(
      {
        "marca": marca,
        "categoria": categoria,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
      }
    )
    archivo = open("productostienda.json", "w")#abro el archivo en modo escritura
    json.dump(productosenventa, archivo)#guardo la lista en el archivo json
    archivo.close()#cierro el archivo
  elif opcion == 2:
    print("Has seleccionado la opción de ver tu tienda")
    for producto in productosenventa:
      print("--------------------")
      print("Categoría:", producto["categoria"])
      print("Marca:", producto["marca"])
      print("Producto:", producto["nombre"])
      print("Cantidad:", producto["cantidad"])
      print("Precio:", producto["precio"], "€")
      print("--------------------")
  elif opcion == 3:
    print("Saliendo del programa...")
    break
