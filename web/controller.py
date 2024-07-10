import sqlite3


def insert_usuarios(nombre,apellido,contrasena,email,correo):
    con = sqlite3.connect("DB/base.db")
    cursor = con.cursor()

    cursor.execute("INSERT INTO usuarios VALUES(?,?,?,?,?)", (nombre,apellido,contrasena,email,correo))

    con.commit()
    con.close()

def crear_tabla():
    con = sqlite3.connect("DB/base.db")
    cursor = con.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre VARCHAR2,apellido VARCHAR2,contrasena VARCHAR2,email VARCHAR2,correo VARCHAR2)")

    con.commit()
    con.close()


def select_usuarios():
    con = sqlite3.connect("DB/base.db")
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    print(datos)

    con.commit()
    con.close()
    return datos

crear_tabla()

