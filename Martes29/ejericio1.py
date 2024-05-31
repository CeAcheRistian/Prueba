#ORM (object relation maps) es para mapear un codigo sql a codigo de python, para no tocar sql directamente
#Se usan clases para sustituir codigo de SQL

from sqlalchemy import create_engine # Se importa el motor de bases de datos

#ORM es una submodulo de sqlalchemy. El sessionmaker contine comandos como execute
from sqlalchemy.orm import sessionmaker, declarative_base 
#Declarative_base es la clase padre para heredar a las clases que contiene a sql

#Column es literalmente es la columna de las tablas. Si se trabaja con datos de tipo entero o cadenas, es necesario importarlos también
from sqlalchemy import Column, Integer, String 
#Tambien se puede importar for in key y con este ligas una tabla con otra

#Se configuran las conexiones
engine = create_engine("sqlite:///basesqlalchemy.db") #sqlalchemy es independiente de sqlite

#Instancia del motor y el nombre
Sesion = sessionmaker(bind = engine) #Es como un portal de conexion, es decir, cuantas conexiones se pueden tener
sesion = Sesion() #Se necesita una instancia para crear y hacer uso de base y ejecutar sentencias

base = declarative_base() #Se crea la base

#Con ORM ya no se trabaja directamente con SQL, sino con Python directamente, usando clases, las cuales contendrán las tablas y contenidos
class Estudiante(base): #Modelado de sql en clases de Python
    __tablename__ = 'estudiante' #Nombre de la tabla
    estudiante_id = Column(Integer, primary_key = True) #Propiedad principal, con su llave primaria
    nombre = Column(String) #Propiedades

    def __str__(self): #Imprime el valor, en este caso el nombre, porque al mandar a llamar a la tabla o sus propiedades, imprimiría una dirección de memoria
        return self.nombre
    
if __name__ == "__main__":
    base.metadata.create_all(engine) # Es para crear la tabla con todos los datos insertados en la clase
    #pedro = Estudiante(estudiante_id = 1, nombre = "Pedro") 
    #sesion.add(pedro)
#Estas lineas se ejecutan 1 sola vez, ya que se especifica el id, y si se vuelve a ejecutar sin modificar el id, se queja el interprete

    sesion.commit()
    estudiantes = sesion.query(Estudiante).all() #Se guarda la info
    for i in estudiantes:
        print(i)

"""El modelo vista controlador MVC propone dividir el contenido del funcionamiento del programa
en 3 archivos: models, para modelos. Vista de views y Controlador como daw o controller este va directo a la base de datos
El 1ro es de la 17 a la 25, el 2do de a 1 a la 15 y el 3ro de la 25 a 32 """
#Con sqlalchemy se pueden manejar de mejor manera, mas eficiente grandes cantidades de informacion
