<?php
// Establecer la conexión a la bd MySQL
$mysqli = new mysqli("db", "root", "test", "dbname");

// Verifica la conexión
if ($mysqli->connect_error) {
    die("Error de conexión: " . $mysqli->connect_error);
}

// Obtiene los datos del formulario
$nombre = $_POST["nombre"];
$apellido = $_POST["apellido"];

// Inserta los datos en la db
$sql = "INSERT INTO Person (name, apellido) VALUES ('$nombre', '$apellido')";

if ($mysqli->query($sql) === TRUE) {
    //echo "Registro exitoso";
} else {
    echo "Error al registrar los datos: " . $mysqli->error;
}

// Cierra la conexión a la db
$mysqli->close();
?>
<script>
window.location.href="index.php"
</script>