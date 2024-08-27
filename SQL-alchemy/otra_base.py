import sqlite3

con = sqlite3.connect('base1.db')
cursor = con.cursor()

def crear_tabla():
    #Las variables pueden ir en mayusculas pero por convencion no van así
    cursor.execute('''
        CREATE TABLE semestre(
            semestre_id NUMBER(18,0) NOT NULL PRIMARY KEY,
            ANIO NUMBER(4,0) NOT NULL,
            FECHA_INICIO DATE NOT NULL,
            FECHA_FIN DATE NOT NULL
        )
        '''
    )

    cursor.execute('''
        CREATE TABLE estudiante(
			estudiante_id NUMBER(10) NOT NULL,
			nombre VARCHAR2(90) NOT NULL,
			direccion VARCHAR2(90) NOT NULL,
			calificacion NUMBER(10),
			grado_actual VARCHAR2(90) NOT NULL	
			)
		'''
	)

    cursor.execute("INSERT INTO estudiante VALUES(1, 'Christian Monroy', 'Tlalpan', '10', '6to semestre')")
    cursor.execute("INSERT INTO estudiante VALUES(2, 'Galileo Cabrera', 'Xochimilco', '10', '8to semestre')")
    cursor.execute("INSERT INTO estudiante VALUES(3, 'Gustavo Madero', 'Tlahuac', '8', '2do semestre')")

#Crearemos un menu interactivo para ver, insertar, eliminar y actualizar datos de la tabla
def insertar_tabla():
    tabla_nombre = input('En que tabla desea insertar?: ')
    datos = input('Que datos desea insertar?: ')
    cadena = f"INSERT INTO {tabla_nombre} VALUES({datos})"
    cursor.execute(cadena)
    con.commit()

def eliminar_tabla():
    t = int(input("Desea eliminar:\n1.-Tabla\n2.-Dato de una tabla\n> "))
    if t == 1:
        tabla_nombre = input('Que tabla desea eliminar?: ')
        cadena = f"DELETE FROM {tabla_nombre}"
        cursor.execute(cadena)
        con.commit()
    elif t == 2:
        #Cachamos una exepcion por si el id no existe y no vaya a romper
        try:
            tabla_nombre = input('De que tabla desea eliminar: ')
            ids = input("Cual es el id del campo a eliminar: ")
#Para eliminar un campo específico de una tabla se ocupa la sentencia DELETE FROM tabla WHERE criterios a cumplir
            cadena = f"DELETE FROM {tabla_nombre} WHERE {tabla_nombre}_id = {ids}"
            cursor.execute(cadena)
            con.commit()
        #Cachamos todas las excepciones y le damos un apodo
        except Exception as e:
            con.commit()
            print(f"Ocurrio el error {e}")

def actualizar_tabla():
    tabla_nombre = input("De que tabla deseas actualizar: ")
    campo = input("Que dato deseas actualizar: ")
    nuevo_dato = input("Dame el nuevo dato: ")
#Con la sentencia UPDATE tabla SET campo = valornuevo Se actualiza el valor de un campo
    cadena = f"UPDATE {tabla_nombre} SET {campo} = {nuevo_dato}"
    cursor.execute(cadena)
    con.commit()

def ver_tabla():
    tabla_nombre = input("Que tabla deseas visualizar?: ")
    cadena = f"SELECT * FROM {tabla_nombre}"
    for row in cadena:
        print(row)
    con.commit()

while True:
    try:
        crear_tabla()
        while True:
            opcion = int(input("Que deseas hacer?\n1.-Insertar\t2.-Eliminar\t3.-Actualizar\t4.-Ver valores\t5.-Salir\t6.-Insertar comando sql\n>>"))
            if opcion == 1: insertar_tabla()
            elif opcion == 2: eliminar_tabla()
            elif opcion == 3: actualizar_tabla()
            elif opcion == 4: ver_tabla()
            elif opcion == 5: break
            elif opcion == 6:
                #Se puede interactuar directamente con la tabla con comandos en la consola
                command = input("SQL>")
                cursor.execute(command)
    except:
        print('Ocurrio un error, se cerrará la base')
        con.close()
        break

crear_tabla()
