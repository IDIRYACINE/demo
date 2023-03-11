package com.idir.tp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class MysqlHelper {
    private Connection connection = null;

    private PreparedStatement preparedStatement = null;

    private ResultSet resultSet = null;

    private final static String tableName = "master";
    private final static String databaseName = "cratt";
    private final static String glassFishJdbc = "jdbc/cratt";

    private static MysqlHelper instance = null;

    public static MysqlHelper getInstance() {
        if (instance == null) {
            instance = new MysqlHelper();
        }
        return instance;
    }

    private MysqlHelper() {
    }

    public void connectGlassFish() {
        try {
            Context initialContext = new InitialContext();

            DataSource dataSource = (DataSource) initialContext.lookup(glassFishJdbc);
            connection = dataSource.getConnection();
            createTableIfNotExists();

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void connect() throws Exception {
        try {
            String username = "root";
            String password = "idir";
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/" + databaseName,
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

        System.out.println(personnes.size());

        return personnes;
    }

    public boolean registerPersonne(String nom, String prenom, String code) {
        try {
            preparedStatement = connection.prepareStatement("INSERT INTO " + tableName + " VALUES(?,?,?)"
            + " ON DUPLICATE KEY UPDATE nom = VALUES(nom), prenom = VALUES(prenom)");
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

    public void deletePersonne(String code){
        try {
            preparedStatement = connection.prepareStatement("DELETE FROM " + tableName + " WHERE code = ?");
            preparedStatement.setString(1, code);
            preparedStatement.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


    private void createTableIfNotExists() {
        try {
            preparedStatement = connection.prepareStatement("CREATE TABLE IF NOT EXISTS " + tableName
                    + " (nom VARCHAR(255), prenom VARCHAR(255), code VARCHAR(255) PRIMARY KEY)");
            preparedStatement.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void disconnect() {
        try {
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        
    }

}
