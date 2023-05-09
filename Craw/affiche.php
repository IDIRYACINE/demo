<?php 

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $notes = $_POST['note'];
    foreach ($notes as $note) {
        echo "$note<br>";
    }
}

?>