archivo = open("clientes.csv", "r")
conjunto_datos = []
lineas = archivo.readlines()

for linea in lineas:
  partido = linea.split(",")
  conjunto_datos.append(partido)

print(conjunto_datos)
