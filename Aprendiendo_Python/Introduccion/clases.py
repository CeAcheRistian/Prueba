#Las clases 
#Para hacer una clase se usa la palabra reservada class seguido del nombre. Con la nomeclatura de CamelCase
#Las clases pueden poseer métodos y atributos.
class Usuario:
    pass

#Las clases pueden instancias objetos que serán del tipo de la clase. Puede o no llevar argumentos que inicialicen los atributos de la clase
chris = Usuario()

#Existen dos tipos de atributos, los atributos de clase y los atributos de la instancia
#Los atributos de clase le pertenecen a la clase, para utilizarlos, se debe usar la clase. Los de instancia, le pertenecen a un objeto y para usarlos se trabaja con el objeto
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

#La idea de las clases es que los objetos que sean instancias de la clase tengan que poseer los atrbutos y métodos de la clase

#Los métodos son funciones dentro de una clase, pero debe poseer un parámetro al menos para ser considerado método, 
class Animal():
    def inicializador(self):
        #el parámetro por defecto es self, este parámetro hace referencia al objeto de la clase, como puede haber muchos objetos, self se intercambia por el objeto
        self.extremidades = 4 #Estos atributos se van a añadir al objeto, siempre y cuando se llame a este método
        self.estado = "vivo"

perro = Animal() #Para este momento, la instancia de la clase está vacía, no posee nada (se puede verificar con: perro.__dict__)
perro.inicializador() #en tiempo de ejecución se le añadiran los atributos del método inicializador(). El parámetro será el objeto

class Vehiculo():
    def ini(self,puertas,llantas): #El método inicializador puede recibir más parámetros
        self.puertas = puertas #Se está inicializando los atributos con un valor específico para cada instancia de la clase
        self.llantas = llantas

moto = Vehiculo()
moto.ini(0,2) #Se especifican los parámetros que no sean self, los cuales serán atributos de este objeto

#Existe el método __init__ el cual es justo un inicializador de atributos, el cual se manda a llamar automáticamente cuando se crea una instancia de la clase

class Estudiante():
    #el método init se sobreescribe y es así, porque todas las clases heredan de la clase Object
    #Para los parámetros, son como las funciones, aceptan valores por defecto
    def __init__(self,nombre='',edad=0): #Cada instancia de la clase deberá especificar dos atributos y uno extra será por default
        self.nombre = nombre
        self.edad = edad
        self.matricula = '000000'

alumno1 = Estudiante("Juan", 18)
print(alumno1.__dict__)

#Las clases pueden heredar de otras clases, adquiriendo los métodos y atributos de la clase padre. Todas las clases heredan de Object
class Mascota:
    def comer(self):
        print('ñam')
    def dormir(self):
        print('Zzzzz')

#Para notar la herencia se escribe la clase padre en los parentensis
class Perro(Mascota):
    pass

bibi = Perro() #El objeto es una instancia de la clase Perro, pero esta hereda de Mascota, así que puede usar los métodos y atributos de la clase padre
bibi.comer()

class Felino():
    pass
#Una clase puede heredar n cantidad de veces, es decir, un padre tiene muchos hijos
#Y se puede heredar de más de una clase, es decir, un hijo puede tener varios padres
class Gato(Mascota,Felino):
    #Las clases hijas puede sobreescribir o sobrecargar los métodos de la clase pabre. Para que los comportamientos se adecuen a las necesidades de la clase hija
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print('rico')
        #Con la función super,accedemos al padre inmediato y ejecutamos los métodos de la clase padre
        super().comer() #Si dentro del método comer de la clase padre llamásemos al método super, se encadenaría la ejecución de los métodos
    

yue = Gato()
yue.dormir() #Lo que hace Py en este paso, es buscar primero en la clase Gato, como no encuentra el método dormir, lo busca en las clases de donde hereda de IZQUIERDA a DERECHA
#Es decir, primero busca en Mascota, luego en Felino, si no lo encuentra, podría buscar en la clase que hereda de estas dos, que podría ser Animal.
#Si varias de las clases poseen el método a llamar, se utilizará el primero que se encuentre.

#Existen dos tipos de métodos, los de instancia (le pertenecen a los objetos o instancias) y los de clase, que le pertenecen a la clase
class Circulo:
    pi = 3.14159
    #Se necesita un objeto que represente a la clase y por convencion es cls. Sin el decorador, PY lo toma como un método de instancia y no uno de clase
    @classmethod
    def area(cls,radio):
        return cls.pi * (radio ** 2)

resultado = Circulo.area(2) #Ejecutamos los métodos de clase

# Las properties son la forma pythonica de evitar la creación de métodos para obtener y modificar atributos de una clase. Esta función nos ayuda a convertir atributos de una clase en properties o managed attributes.
# Hay dos manera de implementarlo, la primera y mejor, con decoradores
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Radius property."""
        print("Get radius")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print("Set radius")

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

"Con las properties podemos acceder a los atributos de la clase sin necesidad de crear mil métodos para cada uno de los atributos."

# La segunda manera de hacer esto es así con un objeto que sea instancia de la función property y dentro mandamos a llamar a las funciones de la clase:
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

"""Para ambos casos: para acceder a estos solo intanciamos la clase y llamamos"""
circle = Circle(10)
circle.radius
circle.radius = 50
del circle.radius