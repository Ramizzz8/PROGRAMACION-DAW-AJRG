import zipfile

origen = 'miarchivo.txt'

destino = 'comprimidos.txt'

archivo = zipfile.ZipFile(destino, 'w')
archivo.write(origen)
