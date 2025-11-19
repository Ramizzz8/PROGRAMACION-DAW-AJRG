menu []

while True:
  comida = input("Introduce un alimento para añadir al menú: ")
  menu.append(comida)
  print("Tu comida hasta el momento es: ")
  for elemento in menu:
    print("- ", elemento)
