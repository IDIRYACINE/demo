<?php
$p = $_GET['param'];
$conn = new PDO("mysql:host=localhost;dbname=cratt", "root", "");
if ($p != "") {
	$sql = "SELECT * FROM personne where nom like '" . $p . "%' or 
				nom like '% " . $p . "%'";
	$result = $conn->query($sql);
	echo "<select id='listper' >";
	while ($row = $result->fetch()) {
		echo $row[0];
		echo "<option>" . $row[0] . " " . $row[1] . "</option>";
	}
	echo "</select>";
}
?>