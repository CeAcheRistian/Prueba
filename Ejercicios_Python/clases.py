"""
Implementa dos clases que representen las estructuras de Pila y Cola
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

def Clases():
    #Definición de clase   
    class miClase():
        def __init__(self, name, age, language):
            self.name = name
            self.age = age
            self.language = language
    
    
        def print(self):
            print(f"Nombre: {self.name}, Edad: {self.age}, Lenguaje: {self.language}")

    alumno = miClase('Christian', 26, 'Python')
    alumno.print()
    alumno.age = 27
    alumno.print()

    class PilasyColas():
        def __init__(self):
            self.lista = []
        
        def append(self, element):
            self.lista.append(element)


        def pop(self, index):
            if len(self.lista) > 0:
                self.lista.pop(index)
            else:
                print('Eso no es posible')
        
        def count(self):
            return len(self.lista)
        
        def imprimir(self):
            print(self.lista)

    pila = PilasyColas()
    pila.append(3)
    print(pila.count())
    pila.append('hola')
    pila.append(False)
    pila.pop(2)
    pila.imprimir()


Clases()