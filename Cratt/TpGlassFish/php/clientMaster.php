<html>

<body>
    <form method="POST" action="">
        codeMaster : <input type="text" name="codeMaster" /><br>
        <input type="submit" value="recherche" name="rech" />
    </form>
    <?php

    error_reporting(E_ALL);
    ini_set('display_errors', 1);

    if (isset($_POST['rech'])) {
        $code = $_POST['codeMaster'];
        $client =
            new SoapClient("http://idir:8080/cratt/RechercheMaster?wsdl");
        $infoMaster = $client->getMaster(array("codeMaster" => $code));
        if ($infoMaster->return) {
            echo "La personne a une MasterCard";
        }
    }
    ?>
</body>

</html>