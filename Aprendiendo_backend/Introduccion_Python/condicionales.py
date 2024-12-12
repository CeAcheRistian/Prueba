#Estructura de código que permite la ejecución de un bloque de código, dependiendo de algunos criterios a evaluar, es decir, se condiciona al programa
#Por convención de Python se debe identar con 4 espacios para denotar que el código pertenece a otro bloque
#Con el la palabra reservada if, se puede hacer esta condicional. después de la palabra reservada se escribe un valor booleano, si es verdadero, se ingresa al bloque de código
if True:
    pass #Palabra reservada para ignorar el resto del bloque de código y salir de la condicional o ciclo

x = 10
if x < 9:
    print('Nunca va a entrar al bloque')

#Es muy usa; que se usen operadores lógicos dentro de la sentencia if, no se limita a uno solo, pueden ser tantos como se desee, pero se busca ser prolijo

if x == 10 and True:
    pass

#Con la palabra reservada else se puede ejecutar un bloque de código solo si la condicional es falsa
if x == 9:
    pass
else:
    print('Hola, gobernador')   

#Cuando se tengan que evaluar múltiples condiciones existe la sentencia elif:
if x != 5:
    print(1)
elif x == 6 or x == 4:
    print(2)
else:
    print(3)

#El operador ternario permite asignar un valor a una variable es cual está sujeto a una condición, además ahorramos líneas de código y se ve chulo
calificacion = 8
mensaje = 'aprobado' if calificacion >= 7 else 'reprobado'

#Mediante el operador lógico or, es posible asignar valores a variables, dependiendo de la evaluación de las posibles opcioones
#Python lee de derecha a izquierda, manteniendo el primer valor verdadero que se encuentre
valor = 'Chris' or True
valor = False or 0 or [] or 1 #SE ALMACENA EL 1, por ser tomado como verdadero