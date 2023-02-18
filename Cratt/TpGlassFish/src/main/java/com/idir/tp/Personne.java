package com.idir.tp;

public class Personne {
    private final String nom;
    private final String prenom;
    private final String code;
    
    public Personne(String nom, String prenom, String code) {
        this.nom = nom;
        this.prenom = prenom;
        this.code = code;
    }

    public String getNom() {
        return nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public String getCode() {
        return code;
    }

    
}
