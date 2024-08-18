#Las listas (o arreglos) son un tipo de dato que permite almacenar otros tipos de datos, enteros, booleanos, cadenas, diccionarios, inclusive otras listas
#Existen dos formas de crear listas vacías

mi_lista = []
lista2 = list()

#Para que no sean vacías, dentro de los corchetes, se agregan todos los elementos que queramos
mi_lista = [True, 'hola', 23]

#Cada elemento de la lista tiene un índice, es decir, una posición dentro de la lista, porque son listas ordenadas
#           0       1       2
mi_lista = [29, 'cadena', False] #Los índices inician en 0

#Para obtener o acceder a elementos de la lista se especifica el índice del elemento que se quiere y se almacena
primer_elemento = mi_lista[0]

#sin almacenarlo en una variable:
print(mi_lista[1])

#Para acceder al último elemento puede ser complicado en caso que la lista sea muy grande o no sepamos donde acaba, entonces ...
ultimo_elemento = mi_lista[-1]

#Con numero negativos, recorremos la lista de derecha a izquierda
#           -3     -2       -1   
mi_lista = [29, 'cadena', False]

#Para actualizar o modificar elementos de la lista. Igualmente se utulizan índices y el nuevo valor
mi_lista[2] = True

#Se pueden generar sublistas, especificando la lista de la que queremos partir y dentro de los corchetes, se indica donde empieza y donde termina
lista_nombres = ['Christian', 'Alexis', 'Fernanda', 'Karina', 'Gilberto', 'Marco']
sub_lista =  lista_nombres[0:3]
#Esta sublista parte del indice 0 y llega al 2, el 3 no es tomado en cuenta, es decir:
#sub_lista = ['Christian', 'Alexis', 'Fernanda'] <- Así quedaría la sublista
#Si se omite alguno de los dos parámetros, entonces se toma como el resto, es decir, la sublista abarcará todo lo demás
sub_lista = lista_nombres[2:] #En este caso se parte de 'Fernanda' hasta llegar al último elemento, 'Marco'
sub_lista = lista_nombres[:4] #En este caso se parte desde el inicio 'Christian', hasta 'Karina'
sub_lista = lista_nombres[:] #Se obtiene una sublista identica a la lista base

#Se puede generar una sublista a partir de otra, saltando datos, utilizando un tercer parámetro, que indica la cantidad de saltos a dar entre elementos
sub_lista = lista_nombres[1:4:2]
#Esto daría ['Alexis', 'Karina']

#Para obtener la lista en orden inverso se usa:
sub_lista = lista_nombres[::-1]
'''
[star:end] 
[star:] Se obtienen los últimos elementos
[:end] Se obtienen los primeros elementos
[star:end:skip] Se saltan elementos
'''

#Para añadir elementos a la lista, lo cuales se agregarán al final de esta
lista_nombres.append('Felix')

#Si se quiere añadir un elemento en una posición en específico. Lleva dos argumentos, el indice y el elemento.
lista_nombres.insert(1,'Jesús')

lista_apellidos = ['Monroy', 'Hernandez', 'Gutierrez', 'Martinez']

#Se pueden sumar o extender listas con otras listas, desntro de los paréntesis se usa la lista para extender
lista_nombres.extend(lista_apellidos)

#Para eliminar elementos específicos
lista_nombres.remove('Martinez')

#Para eliminar elementos a partir de índices
del lista_nombres[-1] #La palabra reservada del, hace referencia a delete
#también existe el método pop(), puedes darle un índice como argumento, por defecto elimina el último, retorna el valor eliminado
lista_nombres.pop()

#Para eliminar todos los elementos de una lista
lista_apellidos.clear()

numeros = [40, 55, 1, 37, 100, 38]
#Para ordenar una lista, de menor a mayor
numeros.sort()

#Ordenar de forma descendente
numeros.sort(reverse=True)
#Con estos dos métodos, se puede acceder rápidamente al elemento más pequeño y al más grande de la lista
#Pero, existen dos métodos que hacen esto, sin necesidad de ordenarl la lista
min(numeros)#El menor
max(numeros)#El mayor

#Para saber si un elemento está dentro de la lista. Retorna un valor booleano
10 in numeros #tambien se vale: 11 not in lista

#Para saber el indice de un elemento, si existen más elementos, solo retorna el primer índice encontrado    
indice = numeros.index(1)

#Una matriz es una lista de listas, puede ser 2x2 hasta nxn
lista1 = [10,20]
lista2 = [30,40]

matriz = [lista1,lista2] #Matriz 2x2
#Para seleccionar un elemento
matriz[0][0]#Seleccionamos el 10
# [0,0] [0,1]
# [1,0] [1,1]   