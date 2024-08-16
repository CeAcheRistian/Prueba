"""
Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""

def Excepciones():
    def ejemplo():
        try:
            x = 10/0
            print(x)
        except ZeroDivisionError:
            print('no se puede dividir entre 0')
    
    def Exceptions():
        try:
            x = 'hola'
            y = 56
            print(x+y)
        except TypeError:
            print(TypeError)
            print('No se pueden sumar dos objetos diferentes')
        
        try:
            print(Hola)
        except NameError:
            print(NameError)
            print('Las cadenas de texto llevan comillas simples o dobles')
        
        try:
            lista = [1, '']
            for i in len(lista):
                print(i + 1)
        except:
            print(TypeError)
            print('Se está intentando iterar un numero, no una lista o un objeto iterable')

    Exceptions()
Excepciones()