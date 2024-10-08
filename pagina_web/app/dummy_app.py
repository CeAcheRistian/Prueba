from flask import Flask, render_template

#Se crea una variable que almacena nuestra aplicación utlizando la instancia de flask
app = Flask(__name__) #Especifica que este es el archivo principal

#Para escribir o diseñar algo en la página web se crea una función que será un decorador, al cual se le pasará al ruta del navegador
@app.route('/')#Lo que exista dentro de la función se verá reflejado en esta ruta, en este caso es la ruta raíz o principal
def index():
    return('Bienvenido!') #String que se vizualizará en la página

#Ejemplo de otra ruta
@app.route('/hola_mundo')
def hola_mundo():
    return('Hola Mundo')
"""
Otra forma de registar rutas en la web es:
def index():
    return('Hoola')
Definimos la función donde se especifican los cambios y llamamos a app.add_url_ ...
"""

""
#Al hacer el comando pip list se despliegan los modulos/utilidades/herramientas instaladas
#En la lista se encuentra Jinja2, un  lenguaje/motor de plantillas que viene con flask y django para páginas web
#Con jinja se puede renderizar archivos html y mostrarlos en la app web
#Se crea una carpeta de nombre templates, la cual flask reconoce que se encuentren los archivos html
#Después de haber creado la carpeta templates y el html ...

@app.route('/saludar')
def saludar():
    #Con este return se hace la conección entre el html y flask
    #return render_template('index.html', titulo='Página principal') #el param1 es el documento a señalar dentro de templates, el segundo especifica el titulo de la pagina, sin tocar html
    """Una mejor forma de hacerlo es: """
    data = {
        'titulo': 'Página principal',
        'encabezado': 'Hola!'
    }
    return render_template('index.html', data=data)


#Hasta este momento es html puro, pero se necesita más que eso: archivos css y JS
#Se crea la carpeta static le cual flask reconoce al igual que templates. En static se almacenan todo tipo de recursos para la app web
#Dentro de static se crean dos subcarpetas css y js y archivos con extenciones del mismo nombre.
#Después de darle formato en el archivo de css, lo vinculamos con el html.

#Para el archivo js, hacemos casi lo mismo que con el archivo css, se agrega la etiqueta correspondiente en el html y se vincula con el archivo js

#Si se ven reflejados los cambios en los respectivos .css y .js entonces la vinculación/importación entre Python-html-css-js está hecha, esto mediante jinja2/flask

""
#Una de las principales características de jinja2 es poder reutilizar plantillas, es decir, tener 1 plantilla base o layout y de ahí tener una estructura base para todo el sitio
#Así reutilizamos bastante código y una mejor estructura
#Entonces creamos layout.html y pasamos todo el contenido de index.html a layout

@app.route('/contacto')
def contacto():
    data = {
        'titulo': 'Contactos',
        'encabezado': 'Hola'
    }
    return render_template('contacto.html',data=data)

#Ahora vamos a implementar dinamismo en la página. Creamos otra ruta pero se le agrega un numero parámetro, este parámetro va entre <picoparéntesis>
#El nombre que le demos también debe ser el mismo para el parámetro de la función.
#Al ingresar a la nueva url, esta es dinámica con el nombre que se le dote
@app.route('/saludo/<nombre>')
def saludo(nombre): #SE REPITE EL NOMBRE DE LA FUNCIÓN Y SUS PARÁMETROS
    return f'Hola {nombre}'


#para ejemplificar un poco más el dinamismo se hace una suma. Como estamos tratando con números se especifica el tipo de dato obligatoriamente en la ruta
#Cada parámetro se separa con una diagonal /, y también se cacha como parámetro en la función, con el mismo nombre.
@app.route('/suma/<int:valor_1>/<int:valor_2>')
def suma(valor_1: int, valor_2: int) -> int:
    return f'La suma es: {str(valor_1 + valor_2)}' #No se puede imprimir un valor numérico, por eso se castea a una cadena


#Jinja también posee condicionales y ciclos, ejemplo de ello:
@app.route('/lenguajes')
def lenguajes():
    data: dict = {
        'lenguajes' : ['Python', 'JavaScript', 'Cobol', 'Java', 'Kotlin', 'Swift']
    }
    return render_template('lenguajes.html', data = data)


if __name__ == "__main__": #Comprobación que es un archivo principal
    #Con run podemos iniciar el servidor
    app.run(debug=True, port=5000) #Con el parámetro debug, iniciamos el modo de depuración, esto evita que estemos reiniciando el servidor ante cualquier cambio
    """
    Con esta linea se especifica la ruta como primer parámetro y después la función como segundo parámetro
    app.add_url_rule('/',view_func = index)
    """