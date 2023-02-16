<?php

echo "<html><head><meta charset='utf-8'><title>Enregistrement</title></head>";
echo "<body>";


$host = 'localhost';
$user = 'root';
$password = 'idir';

function createDatabaseIfNotExists($conn)
{
    $database = 'cratt';

    if (!$conn->select_db($database)) {
        $sql = "CREATE DATABASE IF NOT EXISTS " . $database;
        $conn->query($sql);
        $conn->select_db($database);
    }


    $sql = "CREATE TABLE IF NOT EXISTS personne(
        nom VARCHAR(30) NOT NULL,
        prenom VARCHAR(30) NOT NULL,
        email VARCHAR(50),
        age INT,
        PRIMARY KEY (nom, prenom)
    )";

    $result = $conn->query($sql);
    if (!$result)
        die('erreur SQL :' . $conn->error);

}

$name = $_POST['nom'];
$lastNAme = $_POST['prenom'];
$email = $_POST['email'];
$age = $_POST['age'];

$conn = new mysqli($host, $user, $password, "");

if ($conn->connect_errno) {
    die("Failed to connect to MySQL: " . $conn->connect_error);
}

createDatabaseIfNotExists($conn);

$result = $conn->query("INSERT INTO personne VALUES('$name', '$lastNAme','$email',$age)");
if (!$result)
    die('erreur SQL :' . $conn->error);

echo 'Vos informations ont été ajoutées.';

$conn->close();

echo $name;
echo '<h1>Vos informations ont été ajoutées.</h1></body></html>';

?>