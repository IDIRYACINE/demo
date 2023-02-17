<%@ page import="java.sql.*" %>

    <html>

    <head></head>

    <body>
        <% String code=request.getParameter("code"); String prenom=request.getParameter("nom"); String
            nom=request.getParameter("prenom"); Class.forName("org.gjt.mm.mysql.Driver"); Connection
            con=DriverManager.getConnection("jdbc:mysql://localhost/GRH","root",""); PreparedStatement
            ps=con.prepareStatement("insert into Personne values (?,?,?)"); ps.setString(1,code); ps.setString(2, nom);
            ps.setString(3, prenom); ps.executeUpdate(); %>
    </body>

    </html>