<?php
$name = $_GET['nom'];
$lastName = $_GET['prenom'];
$email = $_GET['email'];
$age = $_GET['age'];


echo " <FORM Method=\"POST\" action = save.php>";
echo "Nom : <INPUT type=text size=20 name= nom value = $name><br>";
echo "Prénom : <INPUT type=text size=20 name= prenom value = $lastName><br>";
echo "EMail : <INPUT type=text size=20 name= email value = $email><br>";
echo "Age : <INPUT type=text size=20 name= age value = $age><br>";
echo " <INPUT type=submit value=Modifier>";
echo " </FORM>";

?>