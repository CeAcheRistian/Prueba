from typing import List, Tuple, Dict, Final, Union, Any, Optional
#Es posible especificarle al lector que una variable, funcion, conjunto y clase no cambien de tipo de dato
"""Python ignora practicamente esta anotación, es más una ayuda para el lector que para el intérprete de Pyhton"""
#Con la notación <nombre: tipo de dato = valor> se asegura que la variable no cambie de tipo de dato durante la ejecución
cadena: str = 'hola' #Puede ser str, bool, float, int, ...
vacio: None =   None

#Para definir variables y después asignarle un valor es:
cadena2: str
cadena2 = 'holi'

#Otras
numero: int = 1
lista: list = [2,3,None]
dicc: dict = {'llave': 'valor'}

#PARA especificar que un alista, tupla, diccionario, ... contiene elementos de un solo tipo de dato
#Importamos desde typing las clases a usar y se especifica el tipo de dato
tupla: Tuple[int] = (1,2,3)
lista: List[str,int] = ['hola', 90]
dicc: Dict[str,str] = {'123':'345'}

#para las funciones se especifica así. se escribe una flecha para denotar el tipo de dato que se va a retornar
def ejemplo(numero: int, lista: List[int,set,str,None]) -> float:
    pass

#Para las constantes, van en mayúsculas, se importa la clase Final y se eespecifica
CONSTANTE: Final = 3.14159

#Para una variable que puede almacenar uno de varios tipos de datos usamos Union[], se importa
usuario: Union[str,None]
#Ejemplo de Union en una funcion
def ejemplo(number: int) -> Union[None,int]:
    if number == 0: return None
    return number + 1
#La importación y el uso de Union puede ser sustituido por el caracter pipe( | )
variable: int | str = ''

#Para no especificar un tipo de dato de una variable se usa Any importado de typing
variable: Any

#Existen Optional para las variables que pueden ser opcionales. Viene bien especificarlo, pero solo aplica en parámetros que son por default
def ejemplo(parametro: Optional[int] = 10):
    pass

#Se pueden usar variables como Alias
from typing import Tuple

Connection = Tuple[str,str,int]
#El tipo de dato es como la variable declarada arriba
def database_connection(connection:Connection) -> Connection | None:
    if connection[0] != 'root':
        return