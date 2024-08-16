"""
Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""
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

agenda()