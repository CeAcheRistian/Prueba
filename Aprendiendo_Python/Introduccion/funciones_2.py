#Las variables poseen un Scope, su funcionamiento dependerá de en qué bloque de código se encuentren y de que scope tengan

animal='Leon'
def ejemplo():
    animal='Perro' #Se podría creer que el valor de animal, cambiaría para el resto del programa, pero no, solo cambia su valor, dentro del scope de la función
    print(animal) #Aunque posean el mismo nombre de varible, para Python son diferentes
ejemplo()
print(animal) #La variable animal conseva su valor, ya que fue creada fuera de un bloque de código, denominandose el scope global

#Las variables globales pueden ser usadas en todo el código, dentro de funciones, condicionales y ciclos.
#Mientras que las variables locales, son eso, locales, solo pueden ser usadas dentro de su bloque de código donde fueron usadas

#Es posible modificar el valor de una variable global, dentro de un bloque de código, con la palabra reservada global, seguido del nombre de la varible
def ejemplo2():
    global animal
    animal = 'Gato'

#Con la palabra nonlocal, le decimos a Python que las variables a escribir serán las ya existentes, esto para que se afecte a la misma variable y no se cree otra
def fun1():
    b = 1
    def func2():
        nonlocal b
        #Normalmente, es decir, sin el nonlocal, b valdría 4 adentro de la función anidada y fuera de ella valdría 1.
        #Pero con nonlocal, la modifica para los bloques de código locales donde nació la variable
        b = 4
    

#Python permite la anidación de funciones
def func1():
    def func2():
        pass

#Las funciones se consideran como "Ciudadanos de primera clase". Es to quiere decir que las funciones pueden ser asignadas a variables,
# usadas como arugmentos de otras funciones y puede haber funciones que retornen funciones
def centigrados_faren(grados):
    return grados * 1.8 +32

#Asignación a una variable
funcion = centigrados_faren
#Ejemplo de una función siendo mandada como argumento
print(funcion(10))

#Una función lambda o función anónima, es una función que se expresa en una sola línea de código, además no poseen un nombre, ya que realizan tareas pequeñas
#Se requiere una variable que contenga la función, la palabra reservada lambda, seguida de los parámetros a usar, separados con comas, dos puntos y el cuerpo.
#No es necesario escribir un return, ya que se hará automáticamente
funcion_lambda = lambda grados: grados * 1.8 + 32

#Un callback es una función que son utilizadas como argumentos para otras funciones y son estas funciones que las reciben como argumento, quienes las manden a llamar
promedio = lambda *args: sum(args)/len(args)
print(promedio(10,9,8,10))
#Segunda función que filtrará los promedios 
aprobatorio = lambda calificacion: calificacion >= 6

#Aquí se da el callback, se especifica que las variables son funciones por convención. Como la función promedio usa parámetros, entonces los agregamos con un *args
#Funcionan principalmente, donde los programas sean modularizables, ya que puedes sustiruir las funciones que son pasadas como argumentos y sigue funcionando
def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    #Si nosotros no colocamos el asterisco en el args, lo que se estaría pasando sería una tupla, no los argumentos per se
    promedio = func_promedio(*args)
    if func_aprobatorio(promedio):
        print(f"Aprobaste con: {promedio}")
    else:
        print(f"Reprobaste, tu calificación es: {promedio}")

mostrar_mensaje(promedio,aprobatorio,4,1,8,7)   

