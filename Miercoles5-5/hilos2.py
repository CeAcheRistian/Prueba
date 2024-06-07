import funciones 
from threading import Thread
from time import time

hilo1 = Thread(target=funciones.contar)
hilo2 = Thread(target=funciones.imprimir)
inicio = time()

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

final = time()
print("Tiempo transcurrido: ", final-inicio)

