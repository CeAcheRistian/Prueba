"""Los hilos en Python se crean instanciando la clase Thread. Se inicia su ejecución con el método start. 
Para esperar por otro hilo se invoca a su método join. 
Se pueden sincronizar hilos mediante exclusión mutua, semáforos o barreras usando las clases Lock, Semaphore y Barrier, respectivamente."""

"""Para trabajar con hilos haremos uso de la librería threading. Esta librería contiene una clase principal Thread que representa a los hilos.
Además, nos proporciona las clases Lock, RLock, Semaphore, BoundedSemaphore y Barrier que nos permiten sincronizar los diferentes hilos de nuestro programa.
Por otro lado, las clase Event establece un mecanismo sencillo de comunicación entre hilos.
La clase Timer nos permite establecer temporizadores para acciones que deban ejecutarse cuando pasa una cierta cantidad de tiempo.
Finalmente, la clase Condition proporciona un mecanismo para que los hilos queden en espera hasta que se cumpla una determinada condición.
Al margen de todas estas clases, la librería threading posee otras funciones que ofrecen información de los hilos, como active_count o current_thread."""