import pickle

menu = []

while True:
  print("Menú de opciones:")
  print("1.- Añadir comida")
  print("2.- Ver menú")
  print("3.- Guardar en archivo")
  opcion = int(input("Selecciona una opción: "))

  if opcion == 1:
    comida = input("Introduce un alimento para añadir al menú: ")
    menu.append(comida)

  elif opcion == 2:
    print("Tu comida hasta el momento es: ")
    for elemento in menu:
      print("- ", elemento)
  elif opcion == 3:
    archivo = open("menu.bin", "wb")#WB = write binary
    pickle.dump(menu, archivo)
    archivo.close()
    print("Menú guardado en formato binario correctamente.")

