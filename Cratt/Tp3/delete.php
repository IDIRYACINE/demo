<?php



$name = $_GET['nom'];
$lastName = $_GET['prenom'];

$host = 'localhost';
$user = 'root';
$password = 'idir';
$database = 'cratt';
$table = 'personne';

$conn = new mysqli($host, $user, $password, "");

if ($conn->connect_errno) die("Failed to connect to MySQL: " . $conn->connect_error);


$conn->select_db($database);

if($conn->error) die('prb de base de données' . $conn->error);
$q = "delete from $table where nom = '$name' and prenom = '$lastName' ;";
$result = $conn->query($q);

if(!$result) die ('erreur SQL :'. $conn->error );

echo " l'enregistrement a été supprimé avec succé !"; ?>