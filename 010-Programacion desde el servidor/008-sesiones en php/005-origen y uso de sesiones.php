<?php
session_start();
$nombre = "Andres Julian";
$_SESSION['nombre'] = $nombre;
?>
<a href="006-destino con sesiones.php">Ir a la página de destino</a>