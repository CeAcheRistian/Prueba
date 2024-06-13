# Repaso de base de datos

import sqlite3 #Importamos sqlite para trabajar con sql

def base_paises_estudiantes(): #Definimos una funcion que se encargará de la base, y se le da un nombre similar a la base
    con = sqlite3.connect('paises.db') # Se crea una instancia del objeto connect, y se especifica donde se van a guardar los datos
    cursor = con.cursor() #Es necesario un cursor dentro de la base, porque dentro de ella, escribiremos, eliminaremos, leeremos y editaremos datos
    
    cursor.execute( #Con execute definimos la creacion, eliminacion, modificacion, insercion de datos
    #Todos los comandos van con el lenguaje de SQL y entre comillas
    #Las variables van en minuscula
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
    
    #Con CONSTRAINT se crea una restricción en la propiedad, además se especifica el nombre del id que SQL va a leer, por eso el _pk
    #Se especifica NOT NULL cuando se le va a dar un valor que no es nulo por definición
    cursor.execute('''
        CREATE TABLE estudiante(
            estudiante_id NUMBER(10) CONSTRAINT estudiante_id_pk PRIMARY KEY,
            nombre VARCHAR2(90) NOT NULL,
            direccion VACHAR2(90) NOT NULL,
            calificacion NUMBER(10),
            grado_actual VARCHAR2(90) NOT NULL
        )
    ''')

    #Para insertar valores en las tablas en con INSERT INTO tabla VALUES(los valores, separados con comas)
    #Dentro de los valores se especifican en el orden en el que la tabla fue creada    
    cursor.execute("INSERT INTO paises VALUES(1, 'México', 'Americano', 'Espanol', 'Peso Mexicano')")
    cursor.execute("INSERT INTO paises VALUES(2, 'China', 'Asiatico', 'Chino', 'Yuan')")
    cursor.execute("INSERT INTO paises VALUES(3, 'Inglaterra', 'Europeo', 'Inglés', 'Libra Esterlina')")
    cursor.execute("INSERT INTO paises VALUES(4, 'Egipto', 'Africano', 'Egipcio', 'Peso Egipcio')")

    #Ahora a la tabla de estudiantes
    cursor.execute("INSERT INTO estudiante VALUES(1, 'Christian Monroy', 'Tlalpan', '10', '6to semestre')")
    cursor.execute("INSERT INTO estudiante VALUES(2, 'Galileo Cabrera', 'Xochimilco', '10', '8to semestre')")
    cursor.execute("INSERT INTO estudiante VALUES(3, 'Gustavo Madero', 'Tlahuac', '8', '2do semestre')")

    #Después de haber anunciado  los datos a insertar, debemos guardarlos en la tabla
    con.commit()
    #Para saber si lo hicimos bien se recorre la tabla con un ciclo y se imprime
    print('Valores en la tabla paises')
    #Con la sentencia SELECT campo(s) FROM tabla señalamos los campos de la tabla que se especifica
    for row in cursor.execute('SELECT * FROM paises'):
        print(row)

    print('Valores en la tabla estudiante')
    for row in cursor.execute('SELECT * FROM estudiante'):
        print(row)
    
    #Para eliminar tablas es con DELETE FROM 
    cursor.execute('DELETE FROM estudiante')
    con.commit()
    #Y al finalizar, cerramos el acceso a la base
    con.close()
#Si queremos volver a ejecutar por segunda vez el programa, python se va a quejar
#Ya que los id de los campos se van a repetir y las tablas ya han sido creadas
#Para solucionar esto se ocupa la sentencia ...
base_paises_estudiantes()
