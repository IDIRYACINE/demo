package com.idir.tp;

import jakarta.jws.WebMethod;
import jakarta.jws.WebParam;
import jakarta.jws.WebService;

@WebService
public class WebServiceClass {
    @WebMethod(operationName = "somme")
    public int somme(@WebParam(name = "param1") int x, @WebParam(name = "param2") int y) {
        return x+y;
    }
}



