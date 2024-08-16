"""
Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def recursividad():
    def orden_inverso(num:int):
        if num >= 0:
            print(num)
            orden_inverso(num - 1)


    def factorial(num: int):  
        if num < 0:
            print("No se puede calcular el factorial de un número negativo")
            return 
        elif num == 0:
            return 1
        else:
            return num * factorial(num - 1)


    def fibonacci(num: int):
        if num <= 0:
            print("Fibonnacci no tiene posiciones negativas")
            return 
        elif num == 1:
            return 0
        elif num == 2:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    orden_inverso(100)
    print(factorial(5))
    print(fibonacci(9))

recursividad()