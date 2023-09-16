<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type");

print("Entro a php");

    $servername = "db2";
    $username = "root";
    $password = "test";
    $dbname = "dbname";

    // Crear conexión a la base de datos
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verificar la conexión
    if ($conn->connect_error) {
        die("La conexión a la base de datos ha fallado: " . $conn->connect_error);
    }

    // Obtener los datos del formulario
    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];

    // Preparar la consulta SQL
    $sql = "INSERT INTO usuarios (nombre, apellido) VALUES ('$nombre', '$apellido')";

    if ($conn->query($sql) === TRUE) {
        echo json_encode(array('message' => 'Datos guardados exitosamente'));
    } else {
        echo json_encode(array('error' => 'Error al guardar en la base de datos: ' . $conn->error));
    }

    // Cerrar la conexión
    $conn->close();
?>
