"""	
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */
"""
# Pues hay una función enumerate() la cual recibe un tipo de dato iterable y como segundo un posible numero donde se empieza la iteración
# Enumerate() retorna un objeto del tipo enumerate, el cual es iterable, siendo dos objetos los que tiene "dentro", un índice y los elementos de la lista que le pasamos por parámetro.
lista = ["A", "B", "C"]

for indice, l in enumerate(lista):
    print(indice, l)

# Tipo enumerate
print(enumerate(lista))

for i,l in enumerate(lista):
    print(l) if l in lista else 'hola'

# Crea un Enum que represente los días de la semana del lunes
week = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_day(day_number:int):
    #Especificamos que empieza en 1 la enumeración
    weeks = list(enumerate(week, 1))
    print(weeks[day_number - 1])
get_day(1)



class Package():

    def __init__(self, identifier:int, state='pending'):

        states = enumerate(['pending', 'cancelled', 'sent', 'delivered'])

        self.identifier = identifier
        self.state = state

        def change_states(self, state):
            if self.state == 'pending':
                pass



paquete_1 = Package(1)
print(paquete_1.__dict__)
