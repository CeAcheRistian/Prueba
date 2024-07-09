from flask import Flask
from flask import request ##request es para poder consumir a traves de los pequeños clientes. se puede consumir  de 3 formas con args.get, args.form y json
##Se puede enviar la info a traves de 3 formas, un formulario, un argunmento(lo que esta en un url) y un json
app = Flask(__name__)#es el cliente principal
@app.route("/") #es un decorador y con route se especifica la ruta del url
def hello(): 
    return "hello"

@app.route("/hello")
def hello2():
    return "hi"

@app.route("/suma/<int:num1>/<int:num2>/<int:num3>") #Se especifican las variables que se van a usar
def suma(num1, num2,num3): #tambien en los parametros
    num1 = request.args.get("num1", num1) #es una forma de consumir los parametros que se le mandan
    num2 = request.args.get("num2", num2)
    num3 = request.args.get("num3", num3)
    return str(num1+num2+num3)

if __name__ == "__main__":
    app.run(debug=True,port=5002) #el run es para correr el servidor, es necesario para visualizar los cambios
    #El debug es para hacer cambios sin tener que matar el servidor, los cambios se hacen en vivo, port es para cambiar el puerto

    #Existen 3 ramas de desarrollo: QA es para pruebas, Prod o PDR es lo que se manda para consumo de lado del cliente, y Dev, que es el desarrollo
    