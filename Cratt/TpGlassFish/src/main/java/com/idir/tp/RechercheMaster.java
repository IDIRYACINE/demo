package com.idir.tp;


import java.sql.*;

import jakarta.jws.WebMethod;
import jakarta.jws.WebParam;
import jakarta.jws.WebService;

@WebService
public class RechercheMaster {
    private final static String tableName = "master";
    private final static String databaseName = "cratt";

    @WebMethod(operationName = "getMaster")
    public String getMaster(@WebParam(name = "codeMaster") String codeMaster) throws SQLException, ClassNotFoundException {
            Connection con;
            PreparedStatement ps;
            String resultatMaster="";
            Class.forName("com.mysql.cj.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost/"+databaseName, "root", "idir");
            ps = con.prepareStatement("select * from "+tableName+" where code = ?");        
            ps.setString(1, codeMaster);
            ResultSet rs = ps.executeQuery();
            rs.next();
            resultatMaster = "Code Master : "+rs.getString(1)+" Date Expire : "+rs.getString(2)+" Solde : "+rs.getString(3);
            return resultatMaster;
    }
}
