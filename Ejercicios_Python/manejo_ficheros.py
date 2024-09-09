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
global lista_productos
lista_productos = []
with open(archivo, 'w+') as a:

    def ingresar():
        producto = input('Ingresa el nombre del producto: ')
        cantidad = input('Ingresa la cantidad vendida: ')
        costo = input('Ingresa el costo del producto: ')
        
        lista_productos.append(f'{producto} ')
        lista_productos.append(f'{cantidad} ')
        lista_productos.append(f'{costo} \n')
        a.seek()
        a.writelines(lista_productos)
        print(lista_productos)

    def consultar():
        a.seek(0)
        print(a.read())


    def eliminar_productos():
        print('Estos son los productos en la lista:')
        consultar()
        producto_eliminado = input('Escribe el nombre del producto que deseas eliminar: ')
        a.seek(0)
        lista_productos = a.readlines()
        for e in lista_productos:
            if producto_eliminado in e:
                print('ENCONTRADO')
                lista_productos.pop(lista_productos.index(e))
        a.seek(0)
        a.writelines(lista_productos)




    
    ingresar()
    #eliminar_productos()
    consultar()
