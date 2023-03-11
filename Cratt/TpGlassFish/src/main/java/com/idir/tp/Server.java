package com.idir.tp;

import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

public class Server extends HttpServlet {
    private MysqlHelper mysqlHelper = null;

    public Server() {
    }

    @Override
    public void init() throws ServletException {
        try {
            mysqlHelper = MysqlHelper.getInstance();
            mysqlHelper.connectGlassFish();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        String path = request.getRequestURI();

        Pattern pattern = Pattern.compile(".*?cratt/(.*?)(?=\\?|$)");
        String targetPage = "index";

        Matcher matcher = pattern.matcher(path);
        if (matcher.find()) {
             targetPage = matcher.group(1);
        }

       
        String auxilaryParameters = "";
        pattern = Pattern.compile(targetPage + "(\\?.*)?");
        matcher = pattern.matcher(path);
        if (matcher.find()) {
            auxilaryParameters = matcher.group(1);
        }

        if (auxilaryParameters == null){
            auxilaryParameters = "";
        }

        String target = targetPage + ".jsp" + auxilaryParameters;
        System.out.println(target);

        RequestDispatcher rd = request.getRequestDispatcher(target);
        rd.forward(request, response);

    }

    @Override
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        String name = request.getParameter("nom");
        String lastName = request.getParameter("prenom");
        String code = request.getParameter("code");

        mysqlHelper.registerPersonne(name, lastName, code);

        RequestDispatcher rd = request.getRequestDispatcher("/showcase.jsp");
        rd.forward(request, response);
    }
}