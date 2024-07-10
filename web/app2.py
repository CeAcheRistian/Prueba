from flask import Flask
from flask import request, render_template, redirect, flash
import controller as c

app = Flask(__name__)

app.secret_key = "abcd"
@app.route("/") 
@app.route("/index")#tambien puede ser /index o /index/ #Entre esta linea y la funcion no puede haber espacios
def index(): #a la raiz principal se le denomina index
    return render_template("index.html") #se especifica el archivo html, el cual debe estar dentro de una carpeta llamada templates
    #template es el archivo o plantilla para el rellenado de la vista


@app.route("/hello")
def hello(): 
    return render_template("hello.html") 

@app.route("/add", methods= ['POST']) #Existge 4 metodos escenciaels para recibir datos, post para recibir, como un insert, GEt para mandar como un select, PUT para modificar equivalente a un update y DELETE para eliminar
def add(): #Se tiene aque especificar el metodo por el cual se recibe, por defecto es GET
    if request.method == 'POST':#El request es la coneccion entre el front y el back. Es la manera de consumir datos de una api o pagina web
        nombre = request.form["usuario_id"]
        apellido = request.form["ap_pat"]
        contrasena = request.form["ap_mat"]
        email = request.form["direccion"]
        correo = request.form["correo"]
        try: #Usualmente el ingreso de datos del formulario a la base lleva una excepcion, ya que el usuario puede ingresar datos erroneos
            c.insert_usuarios(nombre, apellido, contrasena, email, correo)
        except Exception as e:
            print("Fallo, ", e)
    flash('Usuario Creado')
    return render_template("pelicula.html")

@app.route("/crear")
def crear_cuenta():
    return render_template("crear_cuenta.html")

@app.route("/presentar_usuarios")
def presentar_usuarios():
    datos= c.select_usuarios()

    return render_template("presentar_usuarios.html", datos_usuario= datos)

if __name__ == "__main__":
    app.run(debug=True, port = 5002)