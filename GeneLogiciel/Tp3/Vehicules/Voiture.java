package GeneLogiciel.Tp3.Vehicules;

import java.util.Calendar;

public class Voiture extends Vehicule{
    private double puissance;
    private double kilometrage;
    private double cylenderie;
    private int nbPortes;

    public Voiture(String marque, double prixAchat, double prixCourant, int dateAchat,int nbPorts,double puissance,double kilometrage ,double cylenderie) {
        super(marque, prixAchat, prixCourant, dateAchat);
        this.cylenderie =cylenderie;
        this.puissance =puissance;
        this.nbPortes =nbPorts;
    }

    @Override
    public double calculerPrix() {
        double prix = (1-calculerDecots()) * prixAchat;
        return prix;
        
    }

    @Override
    public void affiche() {
        System.out.println("puissance : " + puissance);
        System.out.println("kilometrage : " +kilometrage);
        System.out.println("cylenderie : " + cylenderie);
        System.out.println("nbPorts : "+ nbPortes);
        
    }

    private double calculerDecots(){
        int dateActuelle =  Calendar.getInstance().get(Calendar.YEAR);
        double decots = (dateActuelle - dateAchat) *0.02;
        decots +=(0.05*(kilometrage/10000));
        if(marque == "Fiat" || marque =="Renault"){
            decots +=0.1;

        }
        else if (marque =="Ferrari" || marque =="Porsche"){
            decots -=0.2;
        }
        return decots;
    }
    
}
