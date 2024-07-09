from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/") 
@app.route("/index")#tambien puede ser /index o /index/ #Entre esta linea y la funcion no puede haber espacios
def index(): #a la raiz principal se le denomina index
    return render_template("index.html") #se especifica el archivo html, el cual debe estar dentro de una carpeta llamada templates
    #template es el archivo o plantilla para el rellenado de la vista


@app.route("/hello")
def hello(): 
    return render_template("hello.html") 

@app.route("/pelicula")
def pelicula():
    return render_template("pelicula.html")

@app.route("/crear")
def crear_cuenta():
    return render_template("crear_cuenta.html")

if __name__ == "__main__":
    app.run(debug=True)