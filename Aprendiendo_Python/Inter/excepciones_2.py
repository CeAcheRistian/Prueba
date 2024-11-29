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