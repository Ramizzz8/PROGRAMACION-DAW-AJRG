php es un lenguaje del lado del servidor que requiere que tengamos un servidor preparado

formas faciles de preparas un servidor

En linux(la buena)
terminal:
sudo apt install apache2 (instalar apache)
sudo apt install php (para instalar php sobre apache)
sudo chdmod 777 -R /var/www/html (para dar permisos a la carpeta)

Y a partir de ese momento:
1.-Todos los archivos se meten dentro de /var/www/html
2.-En el navegador ponemos http://localhost/....

En Windows (la forma mala)

descargar xampp
