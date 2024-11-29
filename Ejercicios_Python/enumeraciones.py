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
listado = ["A", "B", "C"]

for indice, l in enumerate(listado):
    print(indice, l)

# Tipo enumerate
print(enumerate(listado))

for i,l in enumerate(listado):
    print(l) if l in listado else 'hola'

# Crea un Enum que represente los días de la semana del lunes
week = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_day(day_number:int):
    #Especificamos que empieza en 1 la enumeración
    weeks = list(enumerate(week, 1))
    print(weeks[day_number - 1])
get_day(1)

"""from enum import Enum
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
def get_day(number: int):
    print
"""

class Package():

    def __init__(self, identifier, state='pending' ):

        self.identifier = identifier
        self.state = state

    def states_list(self, number):
        states = enumerate(['pending', 'cancelled', 'sent', 'delivered'])

        for index, state in states:
            if number == index:
                return state
    
    def package_sent(self):
        if self.state == 'pending':
            self.state = self.states_list(2)
        else:
            print('No es posible modificar el estado del paquete.')

    def package_delivered(self):
        if self.state == 'sent':
            self.state = self.states_list(3)
        else:
            print('No es posible modificar el estado del paquete.')

    def package_cancelled(self):
        if self.state != 'delivered':
            self.state = self.states_list(1)
        else:
            print('No es posible modificar el estado del paquete.')

    def current_status(self):
        print(f'El estado del paquete con el identificador {self.identifier} es: {self.state}')


paquete_1 = Package(1)
paquete_1.current_status()
paquete_1.package_sent()
paquete_1.current_status()
paquete_1.package_cancelled()
paquete_1.current_status()
paquete_1.package_delivered()
paquete_1.current_status()
print('\n')

paquete_2 = Package(2)
paquete_2.current_status()
paquete_2.package_delivered()
paquete_2.current_status()
paquete_2.package_sent()
paquete_2.current_status()
paquete_2.package_delivered()
paquete_2.current_status()


#       Otra forma de hacerlo: 
""""
from enum import Enum
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4


class Order:

    status = OrderStatus.PENDING

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("El pedido no se puede cancelar ya que ya se ha entregado.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")


order_1 = Order(1)
order_1.display_status()
order_1.deliver()
order_1.ship()
order_1.deliver()
order_1.cancel()
"""