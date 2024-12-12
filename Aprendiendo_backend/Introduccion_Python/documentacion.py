#Es una buena práctica de programación el documentar el código. Usando docstring. Que es un comentario una línea después de la declaración de una función/clase
def ejemplo(): #Con convención se usa triple comilla doble
    """
    En la primera línea se agrega una PEQUEÑA descrión de lo que realiza la función

    Posteriormente se describe los valores de entrada y de salida con los que trabaja la función
    Es permitido escribir un to do list
    TODO:
        *primera cosa
    """
    pass

#El docstring escrito se guardará en el atributo __doc__. En py existen objetos documentables, este tipo de objetos poseen el atributo doc.
#Los objetos documentables son los módulos,clases,métodos y funciones. 
#Se puede imprimir en consola el atributo almacenado
print(ejemplo.__doc__)
#Tambien se puede ver con el método help()
#print(help(ejemplo))

#Es posible testear las funciones con >>> dentro del docstring, simulando que estamos dentro de la consola
def ejemplo_2(v,z):
    """"
    Se colocan los picoparéntesis triples , después el llamado de la función misma con sus arguméntos y un línea después, el resultado que debería ser
    >>> ejemplo_2(10,20)
    30

    >>> ejemplo_2(100,200)
    30 
    Aquí va a dar error porque no es el resultado que sea correcto
    """
    return v+z

#Para correr las pruebas se usa el comando python3 -m doctest <archivo>.py