"""
Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

def pilasyColas():
    def navegar():
        lista = []
        while(True):
            var = input('Escribe una url para navegar, o escribe adelante, atrás o salir: ')
            if var == 'adelante':
                pass
            elif var == 'atras':
                if len(lista) > 0:
                    lista.pop()
            elif var == 'salir':
                print('Saliendo')
                break
            else:
                lista.append(var)
            
            if len(lista) > 0:
                print(f"Te encuentas en la página {lista[len(lista)-1]}")
            else:
                print("Estas en la página de inicio")


    def imprimir():
        lista = []
        while(True):
            var = input('Dame el nombre de tus documentos, manda a imprimir o salir: ')

            if var == 'salir':
                break
            elif var == 'imprimir':
                if len(lista) > 0:
                    print(f'Imprimiendo: {lista.pop(0)}')
                else:
                    print('No hay documentos en la cola')
            else:
                lista.append(var)

            print(f'Documentos por imprimir: {lista}')

    navegar()
    imprimir()        

pilasyColas()