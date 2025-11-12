archivo = open("mapa.txt",'r')

lineas = archivo.readlines()

for linea in lineas:
    if "py" in linea:
        print("###################")
        print("Encontrado! ", linea)

