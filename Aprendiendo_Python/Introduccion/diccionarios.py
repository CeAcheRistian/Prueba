#Estructura de datos que almacena cualquier tipo de dato, son mutables, se modifican sus elementos como su longitud en tiempo de ejecución.
#Los diccionarios no poseen índices, en vez de eso se tiene una llave y su valor correspondiente. Una llave puede ser cualquier cosa inmutable: un entero, una cadena, una tupla, ...

#Diccionario vacío
dicc = {}
dicc = dict()

#LLave:valor. No es posible tener llaves repetidas, valores sí. Se conservan el orden de creación de las llaves, apartir de la versión 3.7 de Python
dicc = {
    1: 'valor',
    'nombre': 'Chris',
    'edad': 27,
    (10,20): True
}

#Para agregar un nueva llave valor a una llave. Se accede con el nombre del diccionarioy corchetes
dicc['apellido'] = 'Monroy'

#Actualizar un valor mediante una llave
dicc[1] = 'uno'

#Para obtener el valor de una llave, si no existe, dará error
valor = dicc['edad']

#Para obtener todas las llaves de un diccionario se usa el método keys()
llaves = dicc.keys()

#Para obtener todos los valores de un diccionario se usa el método values()
valores = dicc.values()

#Para saber ambos, llaves y valores, usamos el método items()
items = dicc.items()

#Los métodos items, keys y values retornan un objeto, este puede ser transformado a una tupla
ejemplo = tuple(dicc.items())

#Segunda forma, recorriendo el diccionario:
for key, value in dicc.items():
    #print(key,value)
    pass

#El método get() nos permite obtener el valor de una llave, si ya llave no existe, se puede crear un valor por default
valor = dicc.get('grado', 'La llave no existe') #Le pedimos el valor de la llave grado, como no existe, retornará el valor que le demos como 2do argumento

#Con el método setdefault() obtenemos el valor de una llave, si no existe, lo agregamos al diccionario 
valor = dicc.setdefault('calificacion', 9)

#Transportando list comprehension a los diccionarios
usuarios = ['Alex', 'Miriam', 'Jenny']
diccionario = {usuario:position +1 for position,usuario in enumerate(usuarios)}
print(diccionario)

#Para eliminar llaves de un diccionario
del dicc['nombre']

#Eliminar un elemento con el método pop(), Retorna el valor de llave eliminada, por defecto elimina la última llave
dicc.pop('edad')

#Para eliminar todas las llaves del diccionario
dicc.clear()