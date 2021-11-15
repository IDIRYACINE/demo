package GeneLogiciel.Tp3.Vehicules;
public class Avion extends Vehicule{
    private String moteur;
    private int heureVol;
   

    public Avion(String marque, double prixAchat, double prixCourant, int dateAchat,int heureVol,String moteur) {
        super(marque, prixAchat, prixCourant, dateAchat);
       this.moteur =moteur;
       this.heureVol = heureVol;

    }

    @Override
    public double calculerPrix() {
        double decots = calculerDecots();
        double prix = (1-decots) * prixAchat;
        return prix;
        
    }

    @Override
    public void affiche() {
        super.affiche();
        System.out.println("moteur : " + moteur);
        System.out.println("heureVol : " +heureVol);
    }

    private double calculerDecots(){
        if(moteur == "HELICES"){
            return 0.1 *heureVol/100;
        }
        else{
            return 0.1*heureVol/1000;
        }
    }
    
}
