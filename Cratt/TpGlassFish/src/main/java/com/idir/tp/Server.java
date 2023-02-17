package com.idir.tp;

import java.io.IOException;

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
        System.out.println("Debug Message : " + path);
        path = path.substring(6);
        System.out.println("Debug Message : " + path);
        RequestDispatcher rd = request.getRequestDispatcher(path + ".jsp");
        rd.forward(request, response);

    }

    @Override
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        String name = request.getParameter("nom");
        String lastName = request.getParameter("prenom");
        String code = request.getParameter("code");

        mysqlHelper.registerPerssone(name, lastName, code);
    }
}