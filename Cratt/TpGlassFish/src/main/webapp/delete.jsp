<%@ page import="java.util.ArrayList" %>
<%@ page import="com.idir.tp.MysqlHelper" %>
<%@ page import="com.idir.tp.Personne" %>
<%
    String code = request.getParameter("code");
    if (code != null && !code.equals("")) {
        MysqlHelper.getInstance().deletePersonne(code);
    }
    response.sendRedirect("showcase.jsp");
%>
