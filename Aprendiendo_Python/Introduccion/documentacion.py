#Es una buena práctica de programación el documentar el código. Usando docstring. Que es un comentario una línea después de la declaración de una función/clase
def ejemplo():
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
print(help(ejemplo))