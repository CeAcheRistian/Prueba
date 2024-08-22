#Las variables poseen un Scope, su funcionamiento dependerá de en qué bloque de código se encuentren y de que scope tengan

animal='Leon'
def ejemplo():
    animal='Perro' #Se podría creer que el valor de animal, cambiaría para el resto del programa, pero no, solo cambia su valor, dentro del scope de la función
    print(animal)
ejemplo()
print(animal) #La variable animal conseva su valor, ya que fue creada fuera de un bloque de código, denominandose el scope global

#Las variables globales pueden ser usadas en todo el código, dentro de funciones, condicionales y ciclos.
#Mientras que las variables locales, son eso, locales, solo pueden ser usadas dentro de su bloque de código donde fueron usadas