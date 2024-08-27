#Un closure es una función la cual puede generar de forma diniámica, a otra función.
#Y esta nueva función, puede  acceder a las variables locales, aún cuando la primera haya finalizado

def saludar(nombre):
    mensaje = f'Hola {nombre}' #Variable local

    def mostrar_mensaje():
        print(mensaje) #Para cuando se ejecute esta línea, la función principal habrá finalizado
    
    return mostrar_mensaje

username = 'Chris'
respuesta = saludar(username)
#Es hasta esa línea que se accede a una variable local, la cual ya no existe, pero la función mostrar_mensaje "recuerda"
respuesta()