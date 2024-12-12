#Los ciclos permiten ejecutar la n candtidad de veces, un bloque de código, hasta que una condición se cumpla o deje de cumplirse.

#El ciclo while. Requiere de un contador, el cual se modificará en cada iteración para no ser un bucle infinito
contador = 1
while contador <= 5:
    #print(contador)
    contador += 1 #contador = contador + 1

#AL igual que un bloque if, es opcional el uso del else después del bloque while

#En Python no existe un ciclo for a secas, sino un for each, este ciclo permite iterar sobre cada elemento de un objeto iterable, como lo son las listas, cadenas, tuplas, diccionarios, ...
lista = [1,2,3,4,5]
#En cada vuelta o iteración, la variable elemento, tomará el valor de cada elemento de la lista
for elemento in lista:
    #print(elemento)
    pass

#Existen dos palabras para modificar el comportamiento de los ciclos, break y continue
#Con break se finaliza de forma inmediata el ciclo, sin importar que se encuentre dentro de un bloque if
for x in range(10):
    for y in range(5):
        if y == 2:  
            break #Pero el break solo finaliza un ciclo, si este se encuentra anidado, el ciclo exterior, continua
        print(y)
    print(' ', x)
#La diferencia entre break y continue, es que continue no rompe el ciclo, solo salta a la siguiente iteración, ignorando las siguientes líneas de código
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)