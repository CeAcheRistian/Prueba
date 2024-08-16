""""
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
import random

def Empresa():
    class Empleado():
        def __init__(self, identificador, nombre) -> None:
            self.identificador = identificador
            self.nombre = nombre
            self.lista_empleados = []

        def agregar_empleado(self, empleado):
            self.lista_empleados.append(empleado)

        def imprimirEmpleados(self):
            for e in self.lista_empleados:
                print(e.nombre)
        
    class Gerente(Empleado):
    
        def __init__(self, identificador, nombre):
            super().__init__(identificador, nombre)
            self.chalanes = []

        def chalan(self, nombre):
            self.chalanes.append(nombre)
            print(f'chalanes: {self.chalanes}')

        def banioExclusivo(self):
            print('Baño de gerentes')

    class Gerente_Proyectos(Empleado):
        sucursal = random.randint(0,100)

        def __init__(self, identificador, nombre):
            super().__init__(identificador, nombre)
            self.chalanes = []

        def chalan(self, nombre):
            self.chalanes.append(nombre)
            print(f'chalanes: {self.chalanes}')
        
        def autoEmpresa(self):
            print(f'La empresa le presta un auto a {self.nombre}')

    class Programador(Empleado):
        def __init__(self, identificador, nombre, lenguajes):
            super().__init__(identificador, nombre)
            self.lenguajes = lenguajes
        
        def codear(self):
            print(f'Escribo que escribo, compilo que compilo {self.lenguajes}')

        def agregar_empleado(self, empleado):
            print(f'Los programadores no pueden agregar empleados, {empleado} no puede ser agregado')
        
    empleado1 = Gerente('1', 'Chris')
    empleado1.banioExclusivo()
    empleado1.chalan('alberto')
    
    empleado2 = Gerente_Proyectos('2', 'Victor')
    print(empleado2.sucursal)
    empleado2.agregar_empleado(empleado1)
    empleado2.autoEmpresa()

    empleado3 = Programador('3', 'Karen', 'Python')
    print(empleado3.lenguajes)
    empleado3.codear()
    empleado3.agregar_empleado('ale')
    empleado2.agregar_empleado(empleado2)
    empleado2.imprimirEmpleados()

Empresa()