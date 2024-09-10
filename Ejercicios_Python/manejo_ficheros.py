import os

archivo = 'CeAcheRistian.txt'
with open(archivo, 'w') as a:
    a.write('Christian Jesús Monroy Gutiérrez\n')
    a.write('27 anios\n')
    a.write('Python')

#Se recomeindo más usar un with, como arriba, por el scope y nos ahorramos el close() del archivo
archivo = open('CeAcheRistian.txt', 'r')
for linea in archivo:
    print(linea)
archivo.close()

archivo = '/home/ceacheristian/py/Prueba/Ejercicios_Python/CeAcheRistian.txt'
os.remove(archivo)

archivo = 'abarrotes.txt'

while True:
    print("1. Añadir producto.")
    print("2. Consultar producto.")
    print("3. Actualizar producto.")
    print("4. Borrar producto.")
    print("5. Calcular venta total.")
    print("6. Calcular venta por producto.")
    print("7. Salir.")

    opcion = input('Qué desea hacer?: ')

    if opcion == "1":
        producto = input('Nombre del producto: ')
        cantidad = input('Cantidad: ')
        precio = input('Precio: ')

        with open(archivo, 'w'):
            archivo.write(producto)
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        pass
    elif opcion == "7":
        print('El archivo se autodestruirá.')
        os.remove(archivo)
        break
    else:
        print('Selecciona una opción válida.')

