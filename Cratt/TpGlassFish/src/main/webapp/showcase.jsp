<%@ page import="java.util.ArrayList" %>
    <%@ page import="com.idir.tp.MysqlHelper" %>
        <%@ page import="com.idir.tp.Personne" %>
            <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

                <html>

                <head></head>

                <body>
                    <h1>showcase</h1>

                    <% ArrayList<Personne> personnes = MysqlHelper.getInstance().loadAllPersonnes();
                    %>

                    <c:set var="personnes" value="<%=personnes%>" scope="request"/>

                        <table>
                            <tr>
                                <th>Code</th>
                                <th>Name</th>
                                <th>Last Name</th>
                            </tr>
                            <c:forEach var="personne" items="${personnes}">
                                <tr>
                                    <td>${personne.code}</td>
                                    <td>${personne.nom}</td>
                                    <td>${personne.prenom}</td>
                                </tr>
                            </c:forEach>
                        </table>


                </body>

                </html>