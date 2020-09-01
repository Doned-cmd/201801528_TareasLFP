import json
import SimpleQL
import webbrowser

lista = []
total = 0
archivo = "data.json"
def lectorJSON(archivo):

    global total

    leer = json.loads(open(archivo).read())

    for corredor in leer:
        usuario = SimpleQL.Usuario(corredor['nombre'],corredor['edad'],corredor['activo'],corredor['saldo'])
        lista.append(usuario)
  
    for i,x in enumerate(lista):
        total = i+1
    crearHTML(total)
    
def crearHTML(numero):
    f = open('reporte.html','w')
 
    pimeraparte = """<html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" 
        integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" 
        integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" 
        crossorigin="anonymous"></script>
    </head> 
    <body>
    <table class="table table-dark">
    <thead>
        <tr>
            <th scope="col">Nombre</th>
            <th scope="col">Edad</th>
            <th scope="col">Activo</th>
            <th scope="col">Saldo</th>
        </tr>
    </thead>
    <tbody>"""


    partefinal ="""
   
    </tbody>
    </table>
    </body>
    </html>"""

    parteintermedia = " "
    for i in range(numero):
        parteintermedia = (parteintermedia  +"<tr>" + "<th scope="+"row"+"> "+ lista[i].Nombre +"</th>"
        + "<td>" + str(lista[i].Edad)+  "</td> "
        + "<td>" +str(lista[i].Activo)+ "</td> "
        + "<td>" +str(lista[i].Promedio)+ "</td> "
        +"</tr>")

    mensaje =  pimeraparte+"""""" + parteintermedia+"""""" + partefinal
    f.write(mensaje)
    f.close()
    webbrowser.open_new_tab('reporte.html')

lectorJSON(archivo)