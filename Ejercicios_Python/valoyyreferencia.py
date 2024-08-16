"""
Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

def valor_y_referencia():
    var = 0
    var1 = 1
    lista = [1]
    lista1 = [10]
    
    def por_valor(variable1: int, variable2: int):
        aux = variable1
        variable1 = variable2
        variable2 = aux
        return variable1, variable2
    
    x,y = por_valor(var, var1)
    print(var, ' ', var1, ' ',x , ' ', y)


    def por_referencia(l1: list, l2: list):
        aux = l1
        l1 = l2
        l2 = aux
        return l1 ,l2
    l3, l4 = por_referencia(lista, lista1)
    print(lista, " ", lista1, " ", l3, " ", l4)

valor_y_referencia()