def ejercicio1():
    for i in range(10,56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)
#ejercicio1()

def funcion(cadena1: str, cadena2: str):
    contador = 0
    for i in range(1,101):
        if i % 3 == 0  and i % 5 == 0:
            print(cadena1 + ' ' + cadena2)  
        elif i % 3 == 0:
            print(cadena1)          
        elif i % 5  == 0:
            print(cadena2)          
        else:
            print(i)
            contador += 1
    return contador
#print(funcion("fizz", "buzz"))

def agenda():   
    lista_agenda = list()

    def insertar_contacto():
        print("Dame el nombre del nuevo contacto: ")
        nombre = input()
        i = 1
        while (i):
            numero = (input("Dame el número del nuevo contacto: "))
            if len(numero) <= 10 and len(numero) > 0 and numero.isdigit():
                int(numero)
                lista_agenda.append([nombre, numero])
                i = 0
            else:
                print('Eso no es un numero')            
        

    def buscar_contacto():
        nombre = input("Dame el nombre del contacto que quieres buscar: ")

        for i in lista_agenda:
            if i[0] == nombre: 
                print(i)
               
    
    def eliminar_contacto():
        nombre = input("Dame el contacto que quieres eliminar: ")
        for i in lista_agenda:
            if i[0] == nombre:
                lista_agenda.remove(i)


    def actualizar_contacto():
        nombre = input("Dame el nombre del contacto que quieres actualizar: ")
        for i in lista_agenda:
            if i[0] == nombre:
                nuevo_nombre = input("Dame el nuevo nombre: ")
                numero = input("Ahora dame el nuevo número ")
                i[0] = nuevo_nombre 
                i[1] = numero 
        print(lista_agenda)


    def menu(numero:int):
        if numero == 1:
            insertar_contacto()
        elif numero == 2:
            buscar_contacto()
        elif numero == 3:
            eliminar_contacto()
        elif numero == 4:
            actualizar_contacto()
        elif numero == 5:
            print("Adiós")
            exit()
        elif numero == 6:
            print(lista_agenda)


    def interaccion():
        while(True):
            print("\nBienvenido a tu primer agenda.")
            print("¿Qué deseas hacer?")
            print("""               1.- Insertar un contacto
                2.- Buscar un contacto
                3.- Eliminar un contato
                4.- Actualizar un contacto
                5.- Salir
                6.- Ver tu agenda""")
            numero = int(input(">>"))
            menu(numero)
    interaccion()            
#agenda()

def palabras():
    def palindromo(palabra1:str, palabra2: str):
        if palabra1 == palabra1[::-1]:
            print(f"{palabra1 } Es palíndromo")
        else:
            print(f"{palabra1} No es palíndromo")

        print(f"¿{palabra2} es un palindomo? {palabra2 == palabra2[::-1]}")


    def anagrama(palabra1:str, palabra2:str):
        print(f"¿{palabra1} es un anagrama de {palabra2}?  {sorted(palabra1) == sorted(palabra2)}")    


    def isograma(palabra1:str):
        dicc = dict()
        for letra in palabra1:
            dicc[letra] = dicc.get(letra,0) + 1

        es_isograma = True
        valores = list(dicc.values())
        longitud_dicc = valores[0]
        for i in valores:
            if i != longitud_dicc:
                es_isograma = False
                break

        print(f"¿{palabra1} es un isograma? {es_isograma}")



    palindromo("caca", "anitalavalatina")
    anagrama("alberca", "cazuela")
    isograma("acondicionar")
#palabras()

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
#valor_y_referencia()

def recursividad():
    def orden_inverso(num:int):
        if num >= 0:
            print(num)
            orden_inverso(num - 1)


    def factorial(num: int):  
        if num < 0:
            print("No se puede un factorial de un número negativo")
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
#recursividad()

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

    navegar()
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
    imprimir()        
#pilasyColas()

def Clases():   
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
#Clases()