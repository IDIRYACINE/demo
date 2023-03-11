<%@ page import="java.util.ArrayList" %>
    <%@ page import="com.idir.tp.MysqlHelper" %>
        <%@ page import="com.idir.tp.Personne" %>
            <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

                <!DOCTYPE html>
                <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">

                    <title>Showcase</title>
                </head>

                <body class="bg-gray-100">
                    <h1 class="text-3xl font-bold text-center my-8">Showcase</h1>

                    <% ArrayList<Personne> personnes = MysqlHelper.getInstance().loadAllPersonnes();
                        %>

                        <c:set var="personnes" value="<%=personnes%>" scope="request" />

                        <table class="border-collapse border-2 border-gray-500 mx-auto">
                            <thead>
                                <tr>
                                    <th class="p-3 border-2 border-gray-500 text-center">Code</th>
                                    <th class="p-3 border-2 border-gray-500 text-center">Name</th>
                                    <th class="p-3 border-2 border-gray-500 text-center">Last Name</th>
                                </tr>
                            </thead>

                            <tbody>
                                <c:forEach var="personne" items="${personnes}">

                                    <tr>
                                        <td class="p-3 border-2 border-gray-500 text-center">${personne.code}</td>
                                        <td class="p-3 border-2 border-gray-500 text-center">${personne.nom}</td>
                                        <td class="p-3 border-2 border-gray-500 text-center">${personne.prenom}</td>
                                        <td class="p-3 border-2 border-gray-500 text-center"> <a href="delete.jsp?code=${personne.code}" class="text-blue-500 hover:text-blue-700">Delete</a></td>
                                        <td class="p-3 border-2 border-gray-500 text-center"> <a href="register.jsp?code=${personne.code}&nom=${personne.nom}&prenom=${personne.prenom}" class="text-blue-500 hover:text-blue-700">Update</a></td>

                                    </tr>
                                </c:forEach>

                            </tbody>
                        </table>
                        <script src="./utility/tailwind.min.js"></script>
                        <link href="./styles/showcase.css" rel="stylesheet">
                </body>

                </html>