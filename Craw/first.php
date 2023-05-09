<?php

$nom = "valeur_nom";
$prenom = "valeur_prenom";
$telephone = "valeur_tel";
$message = "Bonjour $prenom $nom";
echo $message . "<br>";
echo "Votre téléphone est $telephone<br>";

$chaine = "coucou ROUCOUcou Paloma";
$resultat = ucfirst(strtolower($chaine));
echo $resultat . "<br>";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombreEtudiants = $_POST['nombreEtudiants'];
    echo "<form action='notes.php' method='POST'>";
    for ($i = 1; $i <= $nombreEtudiants; $i++) {
        echo "Etudiant $i - Nom : <input type='text' name='nom[]'><br>";
        echo "Etudiant $i - Note : <input type='text' name='note[]'><br><br>";
    }
    echo "<input type='submit' value='Enregistrer'>";
    echo "</form>";
} else {
    echo "<form action='' method='POST'>";
    echo "Nombre d'étudiants : <input type='number' name='nombreEtudiants'><br>";
    echo "<input type='submit' value='Valider'>";
    echo "</form>";
}


?>
