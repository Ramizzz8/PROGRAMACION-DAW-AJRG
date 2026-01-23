menu []

while True:
  print("Menú de opciones:")
  print("1.- Añadir comida")
  print("2.- Ver menú")
  opcion = int(input("Selecciona una opción: "))
<<<<<<< HEAD
  if opcion == 1:
  comida = input("Introduce un alimento para añadir al menú: ")
  menu.append(comida)
  elif opcion == 2:
=======

  comida = input("Introduce un alimento para añadir al menú: ")
  menu.append(comida)

>>>>>>> f886ffe8011f26e59a2456d7f0736f6627cb714a
  print("Tu comida hasta el momento es: ")
  for elemento in menu:
    print("- ", elemento)

