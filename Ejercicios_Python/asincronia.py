'''
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
'''
import datetime
import time
import asyncio #Con asyncio podemos convertir funciones y generadores en procesos asíncronos

#Con la palabra reservada async, esta funcion ya es asíncrona, que puede ejecutarse en segundo plano mientras que otro código es ejecutado
async def ejercicio1(nombre: str, duracion: int):
    print(f"Tarea: {nombre}, Duración: {duracion}, inicio: {datetime.datetime.now().second} segundos")
    #time.sleep(duracion) time.sleep no es una herramienta la cual pueda ser asincrónica, solo para la ejecución un determiando tiempo.
    #Para esperar la ejecución y que si se entre en segundo plano se usa await:
    await asyncio.sleep(duracion)
    print(f"Tarea: {nombre}, fin: {datetime.datetime.now().second} segundos")

#Para ejecutar una función asíncrona se requiere de un contexto asíncrono, es entonces cuando llamamos a asyncio.run()
#asyncio.run(ejercicio1('1',2))


async def ejercicio_asincronia():
    #El módulo gather ejecuta de manera concurrente (en paralelo) las funciones asíncronas que se pasan por parámetros
    #Sin el await no esperamos a que finalice cada una de las funciones, se quiere para la coordinación
    await asyncio.gather(ejercicio1('C',3), ejercicio1('B',2), ejercicio1('A',1)) # Se ejecutan al mismo tiempo.
    #SE EJECUTAN DE MANERA PARALELA PERO CADA UNA ACABA EN SU TIEMPO 
    await ejercicio1('D',1)

asyncio.run(ejercicio_asincronia())