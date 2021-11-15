package GeneLogiciel.Tp3;

import GeneLogiciel.Tp3.Vehicules.Avion;
import GeneLogiciel.Tp3.Vehicules.Voiture;

public class GestionVehicule{

 public static void main(String[] args) {
   
    createAndTestAvion();
    System.out.println("---------------");
    createAndTestVoiture();
    }

 public static void createAndTestVoiture(){
    Voiture voiture = new Voiture("bens", 50, 20, 15111998, 10, 35, 1200, 14111990);
    voiture.affiche();
    System.out.println("Voiture price : " + voiture.calculerPrix());
 }
 public static void createAndTestAvion(){
    Avion avion = new Avion("Helicopter", 200, 100, 22112001, 36, "x63");
    avion.affiche();
    System.out.println("Avion price : " + avion.calculerPrix());
 }   
}