import os
'''
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
'''

archivo = 'abarrotes.txt'
open(archivo, 'a')

def mostrar_productos():
        with open(archivo, 'r') as a:
            a.seek(0)
            print(a.read())

while True:
    print("1. Añadir producto.")
    print("2. Consultar producto.")
    print("3. Actualizar producto.")
    print("4. Borrar producto.")
    print("5. Calcular venta total.")
    print("6. Calcular venta por producto.")
    print("7. Salir.")
    print("8. Mostrar productos")

    opcion = input('Qué desea hacer?: ')

    if opcion == "1":
        producto = input('Nombre del producto: ')
        cantidad = input('Cantidad: ')
        precio = input('Precio: ')

        with open(archivo, 'a') as a:
            a.write(f"{producto}, {cantidad}, {precio}.\n")
            print('Lista de productos: ')
        mostrar_productos()
    elif opcion == "2":
        nombre = input('Nombre del producto a buscar: ')
        with open(archivo, 'r') as a:
            for linea in a:
                if nombre in linea:
                    print(linea)
                    break
            """Otra manera:
            for line in a.readlines():
                if line.split(', ')[0] == nombre: Partimos por coma y espacio, porque así se escribió en la opcion 1
                    print(line)"""
    elif opcion == "3":
        nombre = input('Nombre del producto a actualizar: ')
        with open(archivo, 'r') as a:
            lineas = a.readlines()
        with open(archivo, 'w') as a:
            for linea in lineas:
                if linea.split(', ')[0] == nombre:
                    cantidad = input('Qué cantidad: ')
                    precio = input('Qué precio: ')
                    a.write(f"{nombre}, {cantidad}, {precio}.\n")
                else:
                    a.write(linea)
    elif opcion == "4":
        nombre = input('Qué producto desea borrar: ')
        with open(archivo, 'r') as a:
            lineas = a.readlines()
        with open(archivo, 'w') as a:
            for linea in lineas:
                if nombre != linea.split(', ')[0]:
                    a.write(linea)
    elif opcion == "5":
        suma_precios = 0
        with open(archivo, 'r') as a:   
            for linea in a.readlines():
                precio = int((linea.split(', ')[2]).split('.')[0])
                suma_precios = suma_precios + precio
            print(suma_precios)
    elif opcion == "6":
        pass
    elif opcion == "7":
        print('El archivo se autodestruirá.')
        os.remove(archivo)
        break
    elif opcion == '8':
        mostrar_productos()
    else:
        print('Selecciona una opción válida.')


