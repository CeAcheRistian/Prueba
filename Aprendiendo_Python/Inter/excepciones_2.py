''' Las excepciones, en Python, ocurren cuando el interprete de Python detecta un error, algo que no puede solucionar en tiempo de ejecución, se activa un mecanismo, el cual lanza una excepción.
Si no es manejada de manera correcta, esta finaliza de manera abrupta el programa.
Se usan dos bloques para manejar las expeciones correctamente, el bloque try y el bloque except.
En el bloque try va todo el código el cual creamos que pueda lanzar un tipo de error. 

Existen muchos tipos de errores y todos estos tienen una jerarquia. La clase padre BaseException que se crean las excepciones. Estas se pueden manejar solas o en grupo.

En el bloque except se define que hacer cuando una(s) excepcion ocurre, es el plan b ante el error. Buscando que el programa no finalize de forma abrupta.

Todos los errores son Excepciones, pero no todas las excepciones son errores.'''

# Traceback
'''En español, rastrteao de ejecución, es una lista de llamadas y excepciones que se muestran cuando ocurre algun tipo de error. Se muetsra información detallada sobre la secuencia de eventos que condujeron al error, facilitando la depuración y diagnostico del problema.

Contiene información del archivo, linea y función donde ocurrio el problema asi com olas llamadas a otras funciones. Mostrando el error paso a paso.

El traceback se produce cuando la excepción no es manejada. Si es cachada con un try-except, no se muestra a menos que se le indique de forma explicita (raise)
'''

# Ejemplo de una excepcion cachada
try:
    num1 = 1
    num2 = 0
    div = num1 / num2
    print(div)
except ZeroDivisionError as error:
    print('division entre cero no posible')
    print(error)

    """Existen dos bloques opcionales, else y finally"""
else:
    # El bloque else se ejecuta si el bloque try funciona correctamente, es decir, no hubo ningún error
    pass
finally:
    #El bloque finally se ejecuta siempre, después de todos los anteriores.
    pass

"""
HASTA el momento, nosotros solo cachamos el error ZeroDivisionError, pero que pasa si alguno de las variables almacena una cadena de texto o si quiero dividir con una variable que jamás ha sido nombrada. Debemos prepararnos para todos los tipos de excepciones que nuestro código pueda experimentar.

Para hacer esto, agregamos bloques except con su excepción especifica
"""
try:
    numbers = [0,1,2,3]
    num1 = numbers[1]
    num2 = numbers[100]
    div = num1 / num3
    print(div)
except ZeroDivisionError as error:
    print('division entre cero no posible')
    print(error)

except NameError as error:
    print("Lo sentimos, la variable no existe")
    print(error)

    "Queda en nosotros validar todos los errores posibles."
except IndexError as error:
    print("No es posible ingresar a ese indice")
    print(error)


# Es posible cachar todos los errores habidos y por haber, haciendo referencia a la clase padre ´Exception´.
try:
    numbers = [0,1,2,3]
    num1 = numbers[1]
    num2 = numbers[100]
    div = num1 / num3
    print(div)
except Exception as error:
    print(f"error: {error}, no fue posible continuar con la ejecución")

"Exception hereda de BaseException, se puede utilizar esta base pero no es usual para estos errores."


"""Existe la palabra reservada ´raise´, para enviar una excepción a nuestra voluntad"""
def validate_username(username):
    if len(username) > 6: 
        return True
    else:
        raise Exception("El username debe tener una longitud minima de 6 caracteres")

# Pero levantar la excepcion termina el programa de forma abrupta. Debemos cachar la excepcion que enviamos con un bloque try y except
try:
    v = validate_username("alv")
    print(v)
except Exception as error:
    print(error)