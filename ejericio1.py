#Un orm (object relation maps) es para mapear un sql a codigo de python, apra no tocar sql
#Se usan clases para sustituir part
from sqlalchemy import create_engine # Se importa el motor de bases de datos
from sqlalchemy.orm import sessionmaker, declarative_base #El orm es una submodulo de sqlalchemy. El sessionmaker es el execute
#El declarative es la clase padre para heredar a las clases que contiene al sql
from sqlalchemy import Column, Integer, String #El column es literalmente es la columna de las tablas
#Tabmien se puede importar for in key y con este ligas una tabla con otra

#Se configuran las conexciones
engine = create_engine("sqlite:///basesqlalchemy.db") #sqlalchemy es independiente de sqlite
#Instancia del motor y el nombre
Sesion = sessionmaker(bind = engine) # es como un portal de conexion, es decir, cuantas conexiones se pueden
sesion = Sesion() #Se necesita una isntancia para crear hacer uso de base y ejecutar sentencias

base = declarative_base() #Se crea la base

class Estudiante(base): #Modelado de sql en clases de Python
    __tablename__ = 'estudiante' #Nombre de la tabla
    estudiante_id = Column(Integer, primary_key = True) #Propiedades
    nombre = Column(String)

    def __str__(self): #Imprime el valor, en este caso el nombre
        return self.nombre
    
if __name__ == "__main__":
    base.metadata.create_all(engine) # Es para crear la tabla con todos los datos insertados en la clase
    #pedro = Estudiante(estudiante_id = 1, nombre = "Pedro")
    #sesion.add(pedro)
    sesion.commit()
    estudiantes = sesion.query(Estudiante).all() #Se guarda la info
    for i in estudiantes:
        print(i)

"""El modelo vista controlador MVC propone dividir el contenido del funcionamiento del programa
en 3 archivos: models, para modelos. Vista de views y Controlador como daw o controller este va directo a la base de datos
El 1ro es de la 17 a la 25, el 2do de a 1 a la 15 y el 3ro de la 25 a 32 """
#Con sqlalchemy se pueden manejar de mejor manera, mas eficiente grandes cantidades de informacion
