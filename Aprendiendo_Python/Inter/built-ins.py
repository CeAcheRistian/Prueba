#Las buit-ins son funciones que Python ya tiene establecidas para solucionar problemas de manera sencilla, se usan más en la programación funcional.
#Las funciones son zip, map, enumerate y filter.

lista = [1,2,3]
lista2 = [4,5,6]

#Zip permite combinar elementos de dos o más arreglos, retorna un tipo zip, que puede ser transformado en una tupla, van uno a uno
for resultado in zip(lista,lista2):
    print(resultado)

#Con enumerater se puede contar los elmentos de un objeto que se itera.
for numero,elemento in enumerate(lista):
    print(numero, ' -> ', elemento)

#Con map se puede utlilizar los elementos de un arreglo como parámetros de una función. Funciona perfecto con una función lambda
resultado = list(map(lambda x:x**2,lista)) #el primer argumento de map es la funcion, el segundo el objeto iterable. Map retorna un tipo map, por ende se transforma a lista o tupla
print(resultado)

#Con filter se puede filtrar los valores de un arreglo. Para ello, definimos una función que reciba como parámetro los valores del arreglo y retorne un booleano
resultado = list(filter(lambda x: True if x > 4 else False, lista2))
print(resultado)