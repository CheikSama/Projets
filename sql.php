<?php
$requete='SELECT * FROM Opinion_gauche';
echo $requete;
echo "<br>";


// Pour PC
$lienMySQL=new PDO('mysql:host=localhost;port=3306;dbname=prosopographie', 'root','');

$resultat=$lienMySQL->query($requete);

foreach($resultat as $auteur){
    print_r($auteur);
}
echo "<br>";


$requete2='SELECT * FROM Sejour_etranger';
echo $requete2;
echo "<br>";

$resultat=$lienMySQL->query($requete2);
foreach($resultat as $sejour){
    print_r($sejour);
}
echo "<br>";

$requete3='SELECT * FROM Creation_peinture';
echo $requete3;
echo "<br>";

$resultat=$lienMySQL->query($requete3);
foreach($resultat as $creation){
    print_r($creation);
}

echo "<br>";

$requete4='SELECT * FROM Domaine_litterature';
echo $requete4;
echo "<br>";

$resultat=$lienMySQL->query($requete4);
foreach($resultat as $domaine){
    print_r($domaine);
}

?>