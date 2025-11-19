import pickle
agenda =[]

while True:
  print("Selecciona una opción:")
  print("1.- Insertar registros")
  print("2.- Ver registros")
  print("3.- Guardar registros")
  opcion = int(input("Opción: "))

  if opcion == 1:
    #insertar
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    email = input("Dime tu email: ")
    telefono = input("Dime tu telefono: ")
    agenda.append([nombre, apellido, email, telefono])
  #imprimir
  elif opcion == 2:
    print(agenda)
  elif opcion == 3:
  #guardar
    archivo = open("agenda.pickle", "wb")
    pickle.dump(agenda, archivo)
    archivo.close()
