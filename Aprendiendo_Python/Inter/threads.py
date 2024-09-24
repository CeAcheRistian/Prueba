"""Los hilos en Python se crean instanciando la clase Thread. Se inicia su ejecución con el método start. 
Para esperar por otro hilo se invoca a su método join. 
Se pueden sincronizar hilos mediante exclusión mutua, semáforos o barreras usando las clases Lock, Semaphore y Barrier, respectivamente."""

"""Para trabajar con hilos haremos uso de la librería threading. Esta librería contiene una clase principal Thread que representa a los hilos.
Además, nos proporciona las clases Lock, RLock, Semaphore, BoundedSemaphore y Barrier que nos permiten sincronizar los diferentes hilos de nuestro programa.
Por otro lado, las clase Event establece un mecanismo sencillo de comunicación entre hilos.
La clase Timer nos permite establecer temporizadores para acciones que deban ejecutarse cuando pasa una cierta cantidad de tiempo.
Finalmente, la clase Condition proporciona un mecanismo para que los hilos queden en espera hasta que se cumpla una determinada condición.
Al margen de todas estas clases, la librería threading posee otras funciones que ofrecen información de los hilos, como active_count o current_thread."""

from threading import Thread #Se importa la librería
import threading #Se importa directamente para usar los semaforos
from time import sleep, time #Libreria (sleep) que mantiene pausada el código una cierta cantidad de tiempo.

def imprimir():
    inicio = time()
    print(f'empezamos en: {inicio}')
    sleep(3) #La función tardará 3 segundos en esta línea
    print("Hola, soy la función imprimir")
    fin = time()
    print(f'terminamos en: {fin}')
    print(f'Y tardé: {fin - inicio}')

hilo_1 = Thread(target=imprimir) #Asignamos la función a un hilo de ejecución

hilo_1.start() #Inciamos el hilo
hilo_1.join() #El hilo princial espera a que terminen la ejecución los demás hilos. Quien manda a llamar a join se queda a la espera de los demás hilos

def funcion_A():
    print('funcion A')

def funcion_B():
    print('funcion B')

def funcion_C():
    print('funcion C')

def funcion_D():
    print('funcion D')

hilo_1 = Thread(target=funcion_A)
hilo_2 = Thread(target=funcion_B)
hilo_3 = Thread(target=funcion_C)
hilo_4 = Thread(target=funcion_D)

semaforo = threading.Semaphore(3) #Se crea el semaforo y se seleccionan 4 hilos

with semaforo:
    hilo_1.start()
    hilo_2.start()
    hilo_3.start()
hilo_4.start()

hilo_3.join(timeout=3)
hilo_2.join(timeout=2)
hilo_1.join(timeout=1)
