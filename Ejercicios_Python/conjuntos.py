""""

 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.

 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.

"""
# En python a los conjuntos se les conoce como sets, para entender como funcionan se recomienda la siguiente documentación:
# - https://ellibrodepython.com/sets-python
# - https://www.w3schools.com/python/python_sets.asp
# - https://docs.python.org/es/3.13/tutorial/datastructures.html#sets

"""
Python también incluye un tipo de dato para conjuntos. Un conjunto es una colección no ordenada y sin elementos repetidos. Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas. Los conjuntos también soportan operaciones matemáticas como la unión, intersección, diferencia, y diferencia simétrica.

Las llaves o la función set() pueden usarse para crear conjuntos. Notá que para crear un conjunto vacío tenés que usar set(), no {}; esto último crea un diccionario vacío.

Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:

    Los elementos de un set son únicos, lo que significa que no puede haber elementos duplicados.
    Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
    Sus elementos deben ser inmutables.
"""
conjunto_A = {1,2,3,4,5}
print(conjunto_A)
print(type(conjunto_A)) # -> set

# A diferencia de las listas, en los set no podemos modificar un elemento a través de su índice.

# Los sets se pueden iterar de la misma forma que las listas.
for element in conjunto_A: print(element)

print('\n')

# Con la función len() podemos saber la longitud total del set. Los duplicados son eliminados.
conjunto_B = {1,2,2,4,6}
print(len(conjunto_B)) # -> 4

# Siguiendo la teoría de conjuntos podemos unir, hay dos formas con el operador | o con el método union()
print(conjunto_A | conjunto_B)
print(conjunto_A.union(conjunto_B))

# La intersección es con el método intersection()
print(conjunto_A.intersection(conjunto_B))

# Para añadir un elemento al final usamos add()
conjunto_A.add(7)

# Para eliminar un elemento usamos remove(), especificamos el elemento a eliminar. Si no se encuentra, se lanza la excepción KeyError.
conjunto_B.remove(2)

# El método discard() es muy parecido al remove(), borra el elemento que se pasa como parámetro, y si no se encuentra no hace nada.
conjunto_A.discard(20)

# El método pop() elimina un elemento aleatorio del set.
# El método clear() elimina todos los elementos de set.




print('\n')
# Añadir un elemento al final
conjunto_A = {1,2,3}
conjunto_A.add(4)

# Añadir un elemento al inicio
conjunto_A = {0}.union(conjunto_A)
print(conjunto_A)

# Añade varios elementos en bloque al final
conjunto_B = {10,20,30}
conjunto_A = conjunto_A | conjunto_B
print(conjunto_A)

# Añade varios elementos en bloque en una posición concreta.
conjunto_A = {5,6,8}.union(conjunto_A)
print(conjunto_A)

# Elimina un elemento en una posición concreta.
conjunto_A.remove(8)
print(conjunto_A)

# Actualiza el valor de un elemento en una posición concreta.
conjunto_A.remove(20)
conjunto_A.add(25)

# Comprueba si un elemento está en un conjunto.
25 in conjunto_A

# Elimina todo el contenido del conjunto.
conjunto_B.clear()

# Unión
conjunto_B | conjunto_A

# Intersección
conjunto_A.intersection(conjunto_B)

#Diferencia
conjunto_B - conjunto_A

# Diferencia simétrica
conjunto_B ^ conjunto_A

## Otra forma de resolver esto es con listas y luego castear:
data = [1, 2, 3, 4, 5]
print(f"Estructura inicial: {data}")

data.append(6)
print(f"Añadiendo elemento al final: {data}")

data.insert(0, 0)
print(f"Añadiendo elemento al principio: {data}")

data.extend([7, 8, 9])
print(f"Añadiendo elementos al final: {data}")

data[3:3] = [-1, -2, -3]
print(f"Añadiendo elementos en una posición: {data}")

del data[3]
print(f"Eliminando un elemento concreto: {data}")

data[4] = -1
print(f"Actualizando un elemento concreto: {data}")

print(f"Comprobar si un elemento existe: {-1 in data}")

print(f"Eliminar el contenido: {data.clear()}")