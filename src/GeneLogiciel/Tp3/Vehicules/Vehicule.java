package GeneLogiciel.Tp3.Vehicules;
abstract class Vehicule{
    protected String marque;
    protected double prixAchat;
    protected double prixCourant;
    protected int dateAchat;

    public Vehicule(String marque,double prixAchat,double prixCourant,int dateAchat){
        this.marque = marque;
        this.prixAchat = prixAchat;
        this.prixCourant = prixCourant;
        this.dateAchat = dateAchat;
    }

    public double calculerPrix(){
        return prixCourant;
    }
    public  void affiche(){
        System.out.println("marque : " + marque);
        System.out.println("prixAchat : " + prixAchat);
        System.out.println("prixCourant : " + prixCourant);
        System.out.println("dateAchat : " + dateAchat);

    }

}