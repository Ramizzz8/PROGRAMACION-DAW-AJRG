#Programa venta de entradas a evento
# v0.1 Andres Julian Ramirez Guerrero
# Este programa crea un sistema de venta de entradas que gestiona el aforo de una sala y la recaudación. Debe usar if/elif/else, bucles while, saltos (break/continue), try/except para entradas
aforo_maximo = float(input("Introduce el aforo maximo de la sala: "))
aforo_actual = float(input("Introduce el aforo actual de la sala: "))
aforo_restante = aforo_maximo - aforo_actual
precio_entrada = float(input("Introduce el precio de la entrada: "))
recaudacion_total = aforo_actual * precio_entrada
contador_descanso = 0
entradas_vendidas = 0
aforo_total = aforo_actual + aforo_restante
print(f"Aforo máximo: {aforo_maximo}, Aforo actual: {aforo_actual}, Precio entrada: {precio_entrada:.2f}€, Recaudación total: {recaudacion_total:}€")

while True:
  try:
      numero_entradas = int(input("¿Cuantas entradas quieres comprar?: "))
      if numero_entradas <= 0:
          print("El número de entradas debe ser mayor que cero.")
      elif numero_entradas > aforo_restante:
          print("No hay suficientes entradas disponibles.")
      elif 1 <= numero_entradas <= aforo_restante:
              recaudacion_total += numero_entradas * precio_entrada
              aforo_actual += numero_entradas
              aforo_restante = aforo_maximo - aforo_actual
              contador_descanso += numero_entradas
              print(f"Compra realizada. Entradas compradas: {numero_entradas}")
              print(f"Aforo actual: {aforo_actual}, Aforo restante: {aforo_restante}")
              print(f"Recaudación total: {recaudacion_total:.2f}€")
              if contador_descanso >= 5:
                  print("Hemos alcanzado el límite de entradas vendidas antes del descanso. Espere porfavor.")
                  break
      else:
          print("Numero de entradas no válido.")
  except ValueError:
        print("Por favor, introduce un número válido.")
#Aserciones
assert aforo_restante >= 0.
#imprimir el resumen final y decir si la sala esta llena o cuantos asientos hay disponibles
print("Resumen final:")
print(f"Aforo máximo: {aforo_maximo}")
print(f"Aforo actual: {aforo_actual}")
print(f"Aforo restante: {aforo_restante}")
print(f"Recaudación total: {recaudacion_total:.2f}€")
#Si la sala esta llena
if aforo_restante == 0:
    print("La sala está llena.")
else:
    print(f"Quedan {aforo_restante} asientos disponibles.")


