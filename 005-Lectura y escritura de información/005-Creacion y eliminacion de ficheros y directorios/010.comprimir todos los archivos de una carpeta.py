import zipfile
import os

carpeta = input("Introduce una carpeta: ")

for directorio, carpeteas, archivo in os.walk(carpeta):
    for nombre_archivo in archivos:
        origen = os.path.join(directorio,archivo)
        destino = os.path.join(directorio, archivo + ".zip")
        archivo = zipfile.ZipFile(destino,'w',compression = zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname = nombre_archivo)