<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $notes = $_POST['note'];
    header("Location: AfficheNotes.php");
    exit;
}
?>
