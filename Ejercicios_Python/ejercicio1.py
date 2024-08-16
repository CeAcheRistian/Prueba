## Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
def ejercicio1():
    for i in range(10,56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)
ejercicio1()