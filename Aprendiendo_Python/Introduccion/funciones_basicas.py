variable = 3
#Con la función type() se puede conocer el tipo de dato de una variable
type(variable)

#COn la función print() se muestra en pantalla/consola, como argumento existe sep= Con el cual, al imprimir varios tipos de datos, podemos indicar su separador
print(variable)
print(variable, variable, variable, sep="-") #Esto veremos un guion entre cada impresión

#Con la función input() se obtiene lo que se escriba en la consola. Se pausa la ejecución hasta que se presione enter
#Se puede almacenar lo que se escribe en una variable, el mensaje es opcional pero recomendado
var = input('mensaje')

#Con len() se conoce la longitud de una lista, cadena, diccionario, ...
len([0,'', False])

#Con el método range() podemos generar una secuencia de números, del 0 al n, sirve mucho para condicionales de ciclos for
for i in range(10): #Range puede recibir 3 parámetros en total (inicio de la secuencia, final de la secuencia, salto entre los números) muy similar a [0:10:2] de las listas
    pass