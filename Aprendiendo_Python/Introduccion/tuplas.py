#Las tuplas son una estructura de datos muy similares a las listas, se almacenan en ellas otros tipos de datos
#La enorme diferencia entre las listas y las tuplas, es que las tuplas son inmutables, es decir, no es posible modificar sus elementos en tiempo de ejecución
#Otra diferencia, es en velocidad al momento de recorrer la tupla vs lista, las tuplas son más veloces en eso
#tupla vacía
tupla = ()
tupla = tuple()

#las tuplas también usan indices
#para acceder a los elementos de una tupla, se usan corchetes, como en las listas
tupla = (True, (1,2), 'hola')
elemento = tupla[0]

#También es posible hacer subtuplas
subtupla = tupla[::-1]

#Podemos transformar una lista en una tupla y viceversa con el método list() y tuple()
lista = [1]

nueva_tupla = tuple(lista)
lista = list(nueva_tupla)

#Es posbile almacenar en variables los elementos de una tupla, en orden de aparición
numeros = (1,2,3,4)
uno, dos, tres, cuatro = numeros

#En los casos donde sean más elementos que variables, es posbile usar un asterisco en la variable y se almacenará el resto en una lista
numeros = (1,2,3,4,5,6)
uno, dos, tres, cuatro, *resto = numeros #Se denomina *args, se verá en funciones

#Si no se desea trabajar con el resto de valores se usa *_
numeros = (1,2,3,4,5,6)
uno, dos, tres, cuatro, *_ = numeros

#En caso que se desee trabajar con los últimos elementos
numeros = (1,2,3,4,5,6)
_, dos, *_, cinco, seis = numeros #Es posbile omitir variables con un guión bajo

#Para mezclar listas y tuplas se usa el método zip(), el cual retorna un tipo de dato del tipo zip
lista = [1,3,5]
tupla = (2,4,6)
nueva_tupla = zip(lista,tupla)
nueva_tupla = tuple(nueva_tupla) #Transformamos de tipo zip a tupla y se obtiene una tupla con subtuplas de la mezcla de uno a uno de la lista y tupla anteriores
