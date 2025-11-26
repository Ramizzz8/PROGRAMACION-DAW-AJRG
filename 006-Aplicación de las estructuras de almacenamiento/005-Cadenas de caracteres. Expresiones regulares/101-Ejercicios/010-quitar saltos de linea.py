linea_con_salto = "Esto es una prueba \n, lol"

print("Antes de limpiar:", linea_con_salto)

limpiado = linea_con_salto.replace("\n","") #Reemplaza el salto de linea con "\n" a solo un espacio vacio ""

print(limpiado)
