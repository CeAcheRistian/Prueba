#Este es otro ejemplo de como se trabaja con sql alchemy
#Importamos lo que se usa con sql achemy
from sqlalchemy import create_engine #engine es el punto de entrada a la base de datos
#Es el que permite la entrada de SQLAlchemy a la base

"""SQLAlchemy utiliza el patrón Pool de objetos para manejar las conexiones a la base de datos. 
Esto quiere decir que cuando se usa una conexión a la base de datos, esta ya está creada previamente y es 
reutilizada por el programa. La principal ventaja de este patrón es que mejora el rendimiento de la aplicación, 
dado que abrir y gestionar una conexión de base de datos es una operación costosa y que consume muchos recursos."""


from sqlalchemy.orm import sessionmaker, declarative_base #La sesion es como una transaccion
#Cuando se confirma dicha transaccion se refleja en la base todas las operaciones involucradas
#declarative_base es una clase de la que heredaran todos los modelos y realiza un mapeo a partir de la metainformacion

from sqlalchemy import Column, Integer, String, DateTime #Se usa el objeto Collumn para especificar los datos
#Así como el tipo de dato que son, Integer o String, se especifica por el mapeo entre py y alchemy

engine = create_engine("sqlite:///BasesSQLAlchemy.db") #A la funcion se le pasa una cadena de conexion a la base de datos
#Puede ser una base que ya exista. La conexion no ocurre en este momento, se pospone para cuando sea necesario

"""A pesar de que el lenguaje SQL es universal, cada motor de base de datos introduce ciertas variaciones
propietarias sobre dicho lenguaje. A esto se le conoce como dialecto.
Una de las ventajas de usar SQLAlchemy es que, en principio, no te tienes que preocupar del dialecto a utilizar.
El engine configura el dialecto por ti y se encarga de hacer las traducciones necesarias a código SQL. Esta es 
una de las razones por las que puedes cambiar el motor de base de datos realizando muy pocos cambios en tu código."""

#para crear una sesion se utiliza la funcion maker que está asociada a un engine
Session = sessionmaker(bind = engine)

"""Desde el punto de vista de SQLAlchemy, una sesión registra una lista de objetos creados, modificados o 
eliminados dentro de una misma transacción, de manera que, cuando se confirma la transacción, se reflejan en
base de datos todas la operaciones involucradas"""

#Despues de crear el objeto es necesario mandarlo a llamar para obtener las sesiones
session = Session()

Base = declarative_base() #Se crea una clase llamada Base con el metodo. De esta clase se heredará

#AHORA SI, para trabajar con ORM, se declara una clase, de la cual se realizará el mapeo automático a
#una tabla de SQL. A estas clases también se les llama modelos.

class Cancion(Base):
    __tablename__ = 'cancion' #Este es el nombre de la tabla
    id = Column(Integer, primaty_key = True) #Enseguida se enlistan las propiedades, empezando por el id
#Se tiene que espeficiar el tipo de dato y se acomoda mandando a llamar al metodo Column
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)

    def __str__(self): #Se ocupa este metodo magico para que no nos imprima una direccion de memoria
        return self.titulo #Imprimimos el titulo de la base

if __name__ == '__main__':
    Base.metadata.drop_all(engine) # ????
    Base.metadata.create_all(engine) #Se le indica a SQLAlchemy que cree, si no existen, las tablas de todos
    #los modelos que encuentre en la aplicación.

    song1 = Cancion(id = 1, titulo = 'F', minutos = 5) #Creamos una instancia del modelo que es nuestro
    #primer elemento de la tabla
    
    #Procedemos a guardar los datos especificados anteriormente
    session.add(song1) #Se añade a la sesion
    session.commit() #Se confirman los cambios hechos

    #query funciona para hacer consultas a bases, recibe como parámetro la clase a la que se van
    #a realizar las consultas y devuelve un objeto query. songs es un objeto de tipo query.
    songs = session.query(Cancion).all()
    #Query tiene muchas operaciones. all() sirve para obtener todos los objetos de una tabla o consulta.
    #Devuelve un alista con los objetos devueltos por la consulta
    for song in songs:
        print(songs)#Recorremos e imprimimos dicha lista

