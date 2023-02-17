package com.idir.tp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

public class MysqlHelper {
    private Connection connection = null;

    private PreparedStatement preparedStatement = null;

    private ResultSet resultSet = null;

    private final String tableName = "master";

    public void connect() throws Exception {
        try {
            String username = "root";
            String password = "idir";
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase",
                    username,
                    password);

            createTableIfNotExists();

        } catch (Exception e) {
            throw e;
        }

    }

    public ArrayList<Personne> loadAllPersonnes() {
        ArrayList<Personne> personnes = new ArrayList<Personne>();

        try {
            preparedStatement = connection.prepareStatement("SELECT * FROM " + tableName);
            resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                personnes.add(new Personne(resultSet.getString("nom"), resultSet.getString("prenom"),
                        resultSet.getString("code")));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return personnes;
    }

    public boolean registerPerssone(String nom, String prenom, String code) {
        try {
            preparedStatement = connection.prepareStatement("INSERT INTO " + tableName + " VALUES(?,?,?)");
            preparedStatement.setString(1, nom);
            preparedStatement.setString(2, prenom);
            preparedStatement.setString(3, code);
            preparedStatement.executeUpdate();
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    private void createTableIfNotExists() {
        try {
            preparedStatement = connection.prepareStatement("CREATE TABLE IF NOT EXISTS " + tableName
                    + " (nom VARCHAR(255), prenom VARCHAR(255), code VARCHAR(255))");
            preparedStatement.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
