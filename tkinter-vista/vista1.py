#INterfaces gráficas
#GUI: Grafical User Interface
#Primero importamos tkinter, el modulo para crear widgets visuales
import tkinter as tk #Se le pone el apodo para no escribir tanto jsjs

"""Tkinter funciona mediante widgets, elementos que podemos ir incrustando en la app.
Como puede ser un botón, un input de texto, inclusive, la ventana principal es un widget.
"""
#Creamos una variable que es una instancia de la clase Tk()
app = tk.Tk() #Esto es una representación de la ventana principal de la app
#Puede llamarse app, run o root o main
#Es decir, creamos la ventana principal.

#Variables para guardar datos de una entrada de texto, de tipo stringvar y con StringVar
#Los mapeamos a un widget de la app o ventana principal
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

def fun():
    print("Hola")

#Con el método geometry podemos modificar las dimensiones de la ventana
#           Ancho x Alto
app.geometry("600x300")

#Con el método configure() se modifican un chingo de cosas, colores, bordes, tipos de letra,...
app.configure(background="black")

"""Accedemos a un método de la clase dentro del módulo tkinter con el apodo tk
Dicho metodo de la clase Wm de Window manager, sirve para ponerle un título a la
ventana, en sus parámetros especificamos a qué ventana se desea colocar el título
y seguido de la cadena de texto con el título"""
tk.Wm.wm_title(app, "Mi primera interfaz gráfica")


def cambiar_palabra(): #funcion que nos modifica el widget Label
    palabra.set("Hola "+ entrada.get()) #Con set modificamos datos


#Para agregar 1 botón se ocupan dos pasos
#Al igual que con wm_title se requiere que en los parámetros se especifique a que widget
#se va a meter el botón
tk.Button(
    app, #En donde va el botón
    text="Soy un botón", #Que va a decir el botón
    font=("Arial", 16), #Fuente y dimension de la letra dentro de una tupla
    bg="#00a8e8",#Color de fondo, especificado con su código hexadecimal
    fg="white", #Color del frente al tener al cursor encima del botón, afecta a la fuente de las letras
    command=fun,
    #lambda: print("Hiciste click " + entrada.get()), #A command se le especifica una función a ejecutar
    #En este caso imprime en consola el mensaje
    #Si no se escribe la funcion y solo pasamos el print. Se muestra el mensaje en consola al crear el objeto boton pero no al clickearlo
    #El entrada.get() funciona para que después de haberle pasado un texto al Label, se imprima en consola lo que escribimos, después de hacer click
    
    #Con la siguente linea podemos, en vez de imprimir en cosola, imprimimos en el widget principal, al hacer click en el boton
    #command= cambiar_palabra, #Llamados a la funcion como un objeto y no como una llamada de funcion
    #Peeero, esta funcion inhabilita el texto que diga por defecto el Label
    relief="flat"#Con esto eliminamos la pequeña sombra del botón

#para este punto, ya se configuró el botón, pero no lo hemos colocado todavía
).pack( #Con el método pack, incrustamos el botón en la app
    fill=tk.BOTH, #Con fill hacemos que el boton llene ciertas dimensiones. Con BOTH decimos que se expanda de los dos ejes 
    expand=True #Con expand se expande en toda la pantalla de la app
) 

#Label() es un widget que contiene texto
tk.Label(
    app,
    text="Soy una etiqueta",
    fg="white",
    bg="black",
    justify="center", #El justificado del texto de toda la vida

    textvariable= palabra
#Igualmente llamamos a .pack() para incrustar el widget   
).pack(
    fill=tk.BOTH,
    side="left",
    expand=True
#Como el boton y el texto quieren rellenar toda la ventana, se la reparten a mitades
)

#Entrey nos permite introducir texto
tk.Entry(
    app,
    fg="white",
    bg="gray",
    justify="left",
    textvariable= entrada #Ocupamos la variable  que guarda los strings del input  
).pack( #El pack acomoda de uno debajo de otro. el .grid te pide las coordenadas para insertar 
    
    fill=tk.BOTH,
    expand=True
) #Para este punto ya deberíamos de entender que los argumentos son casi los mismos


"""El punto de tener una interfaz gráfica es tener una comunicación abierta con el usuario
Por lo tanto, tenemos que estar escuchando lo que el usuario clickea, escribe o hace,
para que nosotros hagamos algo con esa interacción
Para eso es el método mainloop() para estar actulizando la app para ir generando cambios
en la pantalla. Recoge los eventos ocurridos y los modica (o no), dependiendo del evento"""
app.mainloop()


