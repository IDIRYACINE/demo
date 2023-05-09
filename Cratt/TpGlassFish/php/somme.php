<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

echo "Starting SOAP client.<br/>";

try {
    $i = $_POST["v1"];
    $j = $_POST["v2"];

    $client = new SoapClient("http://idir:8080/cratt/MyWebService?wsdl");
    $somme = $client->somme(array("param1" => $i, "param2" => $j));

    echo "<p>La somme de $i et $j est : </p>";
    echo $somme->return;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
