"""	
Los archivos logs, van a almacenar todos los errores ocurridos en tiempo de ejecución.
Existe un módulo de nombre Logging, con este modulo es posible imprimir mensajes en consola, pero estos están categorizados según su importancia.
INFO = 10
DEBUG = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

Podemos mostrar mensajes de un cierto nivel o mayor
El módulo info cuenta con 5 funciones con cada categoria
"""
import logging

"Por defecto solo se muestran mensajes mayores o igual a 30, para cambiar esto, modificamos la configuración con la función basicConfig y establecemos el nivel en lo mínimo, que es 10"
#logging.basicConfig(level=logging.INFO)

# logging.info('Mensaje informativo')
# logging.debug('Mensaje de depuración')
# logging.warning('Advertencia!')
# logging.error('ERROOOOR')
# logging.critical('ERROR CRITICO!!!!!')

# print('\n')
"""
Para generar archivos logs a partir de excepciones, dentro de los parámetros de basicConfig, existe un atributo filename en el cual por defecto es None, imprimiendo en consola los errores, si especificamos el nombre de un archivo, los almacenará ahí. Con el modo append.
"""
#logging.basicConfig(level=logging.ERROR, filename='errors.log')
# try:
#     10 / 0
# except Exception as error:

#     logging.error('No es posible dividir entre 0')


# Es posible modificar el formato del mensaje mostrado. Con el parámetro format, en este caso mostramos el la fecha y momento exacto de ejecución, el nivel de error y el mensaje.
logging.basicConfig(level=logging.ERROR, filename='errors.log',
                    format="%(asctime)s | %(levelname)s: %(message)s")
import traceback # Para acceder al traceback y poder almacenarlo se debe importar
try:
    10 / 0
except Exception as error:
    # ALlmacenamos toda la información de la excepción en un diccionario y ese almacenamos
    exception_info = {
        'Mensaje': str(error),
        'Detalles': traceback.format_exc() #Necesitamos importarlo porque en un bloque try-except se omite
    }
    logging.error(exception_info)

"Pero esto de crear y mandar el diccionario se tendría que hacer para cada uno de los bloques try-except, lo cual no es funcional. Esto se resuelve facil, opción 1: una función.  opción 2: Un contexto"

'Importamos contextlib creamos una función que haga justo lo mismo pero con el decorador contextmanager'
import contextlib

"""Con esto llamamos a la función por medio de un contexto, es decir, un bloque with"""
@contextlib.contextmanager
def write_on_log():
    try:
        yield # Se le indica a python que se trabaja la función como un bloque, en esta linea se ejecutará todo lo que haya dentro del with
        "El yield es un placeholder que se sustituirá con el código del bloque with"
    except Exception as error:    
        exception_info = {
            'Mensaje': str(error),
            'Detalles': traceback.format_exc()
        }
        logging.error(exception_info)

with write_on_log():
    print(10 / 0)

"Con esto nos libramos de usar un bloque try-except a cada rato, solo usamos una llamada con with a la función y dentro el código que puede detonar una excepción"