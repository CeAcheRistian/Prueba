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

