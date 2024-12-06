# Introducción a bases de datos relacionales.
Una base de datos es una colección de datos organizada en un formato estructurado.

## Tipos de bases de datos
### Distribuida
Consiste en varias bases de datos situadas en diferentes espacios físicos o lógicos, conectadas entre sí por un sistema de comunicaciones. 

Las bases de datos distribuidas o __Distributed Database Management System (DDBMS)__ se caracterizan por almacenar la información en varias computadoras conectadas entre sí, a las cuáles el usuarios puede acceder desde cualquier sitio como si se tratara de una red local.

Ejemplos:
- Apache Cassandra
- Apache HBase

### NoSQL
Es un sistema de almacenamiento de datos que cuenta con particularidades que las diferencian del otro gran grupo de bases de datos, esto es, las relacionales. 

Son un sistema de almacenamiento de información que __se caracteriza por no usar el lenguaje SQL para las consultas__. Esto no significa que no puedan usar el lenguaje SQL, pero no lo hacen como herramienta de consulta, sino como apoyo. Por ello también se les suele llamar NoSQL o «no solo SQL>>.

Ejemplos:
- Mongo DB
- Cassandra
- Redis

### Documentales
Es una de las principales variantes de las bases de datos no relacionales o NoSQL. Se caracterizan por almacenar la información en registros, cada uno de los cuales funciona como una unidad autónoma de información. 

Al ser un tipo de bases de datos no relacionales, otra de sus principales características es que la información no está contenida en tablas. Por el contrario, están pensadas para el almacenamiento de datos semiestructurados, los cuáles se organizan en documentos con valores asignados.

Ejemplos:
- Mongo DB
- Elasticsearch

### Relacionales
Organiza los datos en filas y columnas, que en conjunto forman una tabla. Los datos normalmente se estructuran en varias tablas, que se pueden unir a través de una llave principal o una llave foránea. 

Un __sistema de gestión de base de datos relacional (RDBMS)__ es una referencia más específica al software de base de datos subyacente que permite a los usuarios mantenerlo. 

Estos programas permiten a los usuarios crear, actualizar, insertar o eliminar datos en el sistema y proporcionan:
- Estructura de datos
- Acceso multiusuario
- Control de privilegios
- Acceso a la red

Ejemplos:
Motores de bases de datos relacionales
- Oracle
- Microsoft SQL Server
- PostgreSQL
- MySQL

## Propiedades ACID (Atomicity, Consistency, Isolation, Durability)
- Atomicidad: todos los cambios en los datos se realizan como si fueran una sola operación. Es decir, se realizan todos los cambios, o ninguno.
- Consistencia: los datos permanecen en un estado consistente de un estado a otro, lo que refuerza la integridad de los datos.
- Aislamiento: la realización de una operación no debería afectar a las otras.
- Durabilidad: después de completar con éxito una transacción, los cambios en los datos persisten y no se deshacen, incluso en caso de falla del sistema.

## Ventajas de las bases relacionales
1. Permite manejar grandes cantidades de datos con puntos de relación entre sí.
2. Las bases de datos relacionales permiten mantener la uniformidad de los datos en todas las aplicaciones.
3. Las bases de datos relacionales garantizan que todas las copias de la base de datos tienen los mismos datos en todo momento.
4. Garantizan que no se produzca la duplicidad de registros.
5. Pueden bloquear el acceso a los datos mientras se están actualizando para evitar conflictos cuando se intentan acceder a los mismos datos en el mismo momento.

## Desventajas de las bases relacionales
1. Son deficientes a la hora de manejar datos gráficos, multimedia, CAD y sistemas de información geográfica, que necesitan un soporte más dinámico.
2. No permiten desarrollar tablas organizadas de forma jerárquica, es decir, no se puede crear un subfila, porque todas las filas están al mismo nivel jerárquico, por tanto no se puede emplear entidades subordinadas.
3. Puesto que acaban segmentándose en diferentes tablas separadas, esto provoca un rendimiento negativo a la hora de hacer consultas y obtener la información deseada.

## SQL (Structured Query Language)
El lenguaje estructurado de consultas apoya la creación y mantenimiento de la base de datos relacional y la gestión de los datos.
Los tipos de instrucciones de SQL:
- DDL: Data Definition Language. Cosas como crear, modificar o eliminar objetos.
- DCL: Data Control Language. Permisos y usuarios.
- DML: Data Manipulation Language. Las sentencias o query como select, insert, update y delete como los más comunes
- TCL: Transaction Control Language.

# Continua en el PDF

# Ejemplos y ejercicios: [aquí](https://tech.io/playgrounds/123318/sql-facilito)