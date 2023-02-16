<?php

echo "<html><head><meta charset='utf-8'><title>Enregistrement</title></head>";
echo "<body>";


$host = 'localhost';
$user = 'root';
$password = 'idir';
$database = 'cratt';
$table = 'personne';


function createDatabaseIfNotExists($conn)
{
    global $database;

    if (!$conn->select_db($database)) {
        $sql = "CREATE DATABASE IF NOT EXISTS $database";
        $conn->query($sql);
        $conn->select_db($database);
    }

    global $table;
    $sql = "CREATE TABLE IF NOT EXISTS $table(
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

function loadAndDisplayPersonneTable($conn)
{
    global $database;
    global $table;

    $result = $conn->query("Select * FROM ".$table."" );
    echo "<table border=\"1\" >\n <caption>Liste des personnes </caption>
    <th> Nom </th> <th> Prénom </th> <th> Email </th> <th> Age </th>";

    while ($row = $result->fetch_row()) {
        echo "<tr> <td>$row[0]</td> <td>$row[1]</td> <td>$row[2]</td> <td bgcolor=\"#00FF00\">".$row[3]."</td>";
        echo "<th> <a href=\"edit.php?nom=$row[0]&prenom=$row[1]&email=$row[2]&age=$row[3]\">Modifier</a></th>";
        echo "<th> <a href=\"delete.php?nom=$row[0]&prenom=$row[1]\">Supprimer</a></th>";
    
    }
    echo "</table>";
}

function upsertPersonne($conn)
{
    $name = $_POST['nom'];
    $lastName = $_POST['prenom'];
    $email = $_POST['email'];
    $age = $_POST['age'];

    $result = $conn->query("INSERT INTO personne VALUES('$name', '$lastName','$email',$age)
        ON DUPLICATE KEY UPDATE email='$email' , age='$age' ;");
    
    if (!$result)
        die('erreur SQL :' . $conn->error);
}


$conn = new mysqli($host, $user, $password, "");

if ($conn->connect_errno) 
    die("Failed to connect to MySQL:" . $conn->connect_error);

createDatabaseIfNotExists($conn);
upsertPersonne($conn);
loadAndDisplayPersonneTable($conn);

$conn->close();

?>