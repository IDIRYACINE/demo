<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1" %>
  <!DOCTYPE HTML>
  <html>

  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>Register</title>

  </head>

  <body id="main">

    <form id="registerForm" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" action="showcase" method="post">
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="code">
          Code :
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="code" type="text" placeholder="Enter code" name="code" value="${param.code}">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="name">
          Name :
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="name" type="text" placeholder="Enter name" name="nom" value="${param.nom}">
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 font-bold mb-2" for="lastname">
          Last Name :
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="lastname" type="text" placeholder="Enter last name" name="prenom" value="${param.prenom}">
      </div>
      <div class="flex items-center justify-center">
        <input
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          id="submitButton" type="submit" value="Register">
      </div>
    </form>


    <script src="./utility/tailwind.min.js"></script>

    <link href="./styles/register.css" rel="stylesheet">
  </body>

  </html>