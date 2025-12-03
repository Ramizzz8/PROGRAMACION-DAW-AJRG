menu []

while True:
  print("Menú de opciones:")
  print("1.- Añadir comida")
  print("2.- Ver menú")
  opcion = int(input("Selecciona una opción: "))
  if opcion == 1:
  comida = input("Introduce un alimento para añadir al menú: ")
  menu.append(comida)
  elif opcion == 2:
  print("Tu comida hasta el momento es: ")
  for elemento in menu:
    print("- ", elemento)

