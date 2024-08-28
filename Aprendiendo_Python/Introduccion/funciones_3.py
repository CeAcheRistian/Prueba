#Un closure es una función la cual puede generar de forma diniámica, a otra función.
#Y esta nueva función, puede  acceder a las variables locales, aún cuando la primera haya finalizado
def saludar(nombre):
    mensaje = f'Hola {nombre}' #Variable local

    def mostrar_mensaje():
        print(mensaje) #Para cuando se ejecute esta línea, la función principal habrá finalizado
    
    return mostrar_mensaje

username = 'Chris'
respuesta = saludar(username)
#Es hasta esta línea que se accede a la variable local, la cual ya no existe, pero la función mostrar_mensaje "recuerda"
respuesta()

"""Un decorador ayuda a reducir líneas de código duplicadas, haciendolo más legible, más fácil de testear y mantener. No se limitan a funciones, pueden ser clases, métodos,...
Un decorador es una función la cual toma como input una función y retorna otra función.
Entonces en los decoradores, hay 3 funciones, la función principal, la función a decorar y la función decorada
Los decoradores sirven para extender funcionalidades a una función.
func_a(func_b):
    return func_c
"""
#Estructura base para un decorador
def decorador(func_base):
    def func_decorada():
        print('Te encuentras dentro de la función ya decorada')
        #Para poder ejecutar la función base, la tenemos que mandar a llamar dentro de la función ya decorada, con el nombre que tiene como argumento
        func_base()
    return func_decorada

#Para especificarle a Python que una función será decorada con un @ y el nombre de la función decoradora
@decorador #Con esto le especificamos a Py que la función saludar será el argumento de la funcion decorador
def saludar():
    print('Hola')
#Para este punto, si mandamos a llamar a la función, no se imprimiría nada, ya que, al ser decorada, se ejecutaría la función ya decorada, es decir, la función anidada al decorador
saludar()

# En caso que la función base tenga argumentos y retorne algo. Se modifica el decorador
def func_decoradora(func_base):
#Al decorar una funcion y ejecutarla, no se ejecuta ella misma, sino la función ya decorada. Por lo tanto, en la función decorada, se colocan los parámetros que recibiría la función base
    def func_decorada(*args, **kwargs):
#Se tienen que passar tal cual los argumentos con *args y **kwargs tanto en la función base como en la función decorada        
        resultado = func_base(*args, **kwargs) #Se agrega en una variable el resultado, ya que la función base también retorna un valor y es justo lo que queremos visualizar en consola
        return resultado
    return func_decorada

@func_decoradora
def suma(a,b):
    return a+b  

resutlado = suma(10,20)
#Si imprimimos el resultado nos dará None, y no la suma. La función decorada debe retornar lo que retorne la función base, esto para poder obtener el valor de la función base
print(resutlado)

