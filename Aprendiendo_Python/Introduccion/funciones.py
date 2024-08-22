#Las funciones son bloques de código, que ejecutan una sola tarea, buscando que el código no sea repetitivo
#Para crear o definir una función se usa la palabra reservada def,después el nombre de la función y sus parámetros en paréntesis.
def mi_funcion():
    #El nombre de la función sigue las normas del snake_case
    pass
#Las funciones no se ejecutan,a menos que sean mandadas a llamar o se almacenen en una variable
mi_funcion() #Pueden ser ejecutadas cuantas veces queramos

#En los parámetros (o valores de entrada) van variables que serán definidas y  posteriormente usadas DENTRO de la función, son OPCIONALES
def sumar(a,b):
    print(a+b) #Estas variables solo existen dentro de la función, no pueden ser llamadas ni modificadas fuera de la función

numero_1 = 10
numero_2 = 20
sumar(numero_1,numero_2) #Los valores de entrada se les llama ARGUMENTOS

#Las funciones pueden retornar valores, para hacer esto existe la palabra reservada return
def restar(n1,n2):
    return n1-n2
#Es posible almacenar el retorno de los valores de una función en una variable
resultado = restar(numero_2,numero_1)
print(resultado)

#Se puede tener parámetros por default, es decir, si no se manda nada como argumento, entonces ese variable tomará ese valor
def area_circulo(radio, pi=3.14): #Sin espacios entre la asignación
    return pi * (radio ** 2)
area_circulo(3) #Argumento para el área, por la posición en la que se los parámetros se crearon
#También es posible especificar el orden
area_circulo(pi=3.141592,area=8)