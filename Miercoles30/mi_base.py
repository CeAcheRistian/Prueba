# Repaso de base de datos

import sqlite3 #Importamos sqlite para trabajar con sql

def base_paises(): #Definimos una funcion que se encargará de la base, y se le da un nombre similar a la base
    con = sqlite3.connect('paises.db') # Se crea una instancia del objeto connect, y se especifica donde se van a guardar los datos
    cursor = con.cursor() #Es necesario un cursor dentro de la base, porque dentro de ella, escribiremos, eliminaremos, leeremos y editaremos datos
    
    cursor.execute( #Con execute definimos la creacion, eliminacion, modificacion, insercion de datos
    #Todos los comandos van con el lenguaje de SQL y entre comillas
        '''
        CREATE TABLE paises(
            pais_id NUMBER(10) PRIMARY KEY,
            nombre VARCHAR(20),
            continente VARCHAR(20),
            lengua VARCHAR2(90),
            moneda VARCHAR2(15)
            )    
        '''
    #Sentencia para crear una tabla es CREATE TABLE nombre ()
    #El primer dato de la tabla es su id, la cual es la llave primaria, como su CURP para las personas
    #También se tiene que especificar el tipo de dato que es la variable, y cuantos datos albergará
    )

    