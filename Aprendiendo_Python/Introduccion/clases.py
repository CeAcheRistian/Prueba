#Las clases 
#Para hacer una clase se usa la palabra reservada class seguido del nombre. Con la nomeclatura de CamelCase
#Las clases pueden poseer métodos y atributos.
class Usuario:
    pass

#Las clases pueden instancias objetos que serán del tipo de la clase. Puede o no llevar argumentos que inicialicen los atributos de la clase
chris = Usuario()

#Existen dos tipos de atributos, los atributos de clase y los atributos de la instancia
#Los atributos de clase le pertenecen a la clase, para utilizarlos, se debe usar la clase. Los de instancia, le pertenecen a un objeto y oara usarlos se trabaja con el objeto
class User:
    name = 'default' #Estos dos son atributos de clase, le pertenecen a la clase y para usarlos se debe usar la clase
    age = ''
#Así se accede a un atributo de la clase
print(User.name)
User.age = "0" #También se permite la modificación de atributos

#Los objetos que son instancias de la clase poseen los atributos y métodos de la clase, pero unos propios.
jesus = User()
jesus.name = 'jesus' #No se modifica el atributo de la clase, sino el atributo de la instancia. Incluso se pueden añadir atributos en tiempo de ejecución
#Python trabaja internamente con el meta-atributo __dict__ .Dentro de este se encuentran todos los atributos que posea el objeto en un diccionario
print(jesus.__dict__)

#Las instancias de la clase deben poseer los mismos atributos