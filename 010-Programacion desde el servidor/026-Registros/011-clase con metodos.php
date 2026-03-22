<?php
session_start();

class Registro {

    public $registro;

    public function __construct() {
        $this->registro = [];

        $this->registro['servidor'] = $_SERVER;
        $this->registro['get'] = $_GET;
        $this->registro['post'] = $_POST;
        $this->registro['sesion'] = $_SESSION;
    }

    // Método para convertir a JSON
    public function convertirJSON() {
        return json_encode(
            $this->registro,
            JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
        );
    }

    // Método para guardar el archivo
    public function guardarArchivo($ruta = "log/") {
        $json = $this->convertirJSON();
        $archivo = $ruta . date('U') . ".json";
        file_put_contents($archivo, $json);
    }
}

// Crear instancia
$registro = new Registro();

// Guardar archivo
$registro->guardarArchivo();
?>