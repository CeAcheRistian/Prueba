# Introducción a Django
La mayoría del contenido viene en las diapositivas.

Después de instalar django, crear el proyecto y correr el servidor, podemos ingresar al endpoint admin/, creado automáticamente en el archivo urls.py. Pero nos pedirá contraseñas.

Pero antes de crearlo debemos migrar las tablas de las bases de datos que ocupa django. De hecho, al correr el servidor nos lo indica en color rojo.

Entonces para migrar ejecutamos: _python3 manage.py migrate_

Ahora si, para crear un usuario administrador y crear contraseñas, ejecutamos: _python3 manage.py createsuperuser_

Después de correr el comando para crear una aplicación, cosa diferente a un proyecto. vamos al archivo views.py de la app, en este caso llamada products.

## Primer hola mundo
En view.py se encuentra toda la lógica de negocio y donde se manda la información al frontend. Comparado con flask, es aquí donde se crean las rutas.

De mientras creamos una función llamada index que tiene por parámetro un objeto request y que retorna una respuesta http con el mensaje hola mundo. Pero esto todavía no está listo, debemos importarla función a un archivo urls, pero dentro de nuestra app. Porque el proyecto tiene su propio archivo urls.py.

Entonces, dentro del urls.py de products, importamos la función y dentro de la lista _urlspatterns_ colocamos la función path (que ya viene por defecto) y dentro como primer parámetro la ruta ('') y como segundo parámetro, la llamada de la función, sin paréntesis.

Ahora, debemos agregar en el archivo urls.py principal, el del proyecto el archivo url de la aplicación. Para hacer esto, nos vamos al urls.py principal, importamos de djando.urls la función include. y dentro de la lista _urlspatterns_ como otro elemento, agregamos otro path pero ahora con la ruta '' que es index y, como segundo parámetro, la llamada a include y como parámetro el path de nuestro archivo urls.py de productos, en este caso es productos.urls

Lo que hace la función includes es tal cual, incluir lo que venga en otros archivos urls.py de aplicaciones dentro del proyecto.

Y listo, se creo el primer hola mundo.

## Creación de modelos
Django ya viene con un ORM integrado, así que no es necesario tratar con la base de datos directamente.
En nuestra aplicación productos, viene un archivo de nombre models.py

Para crear los modelos se crean clases que heredan de Model, pero django ya nos está haciendo una importación, entonces debemos heredar de models.Model

Como en otros ORMs, las variables a definir son los campos de las tablas, pero no se llama directamente a un string o un charfiel, se llama a través del objeto models, que django nos provee.

Un campo nuevo (para mi) es el de ImageField, para las imagenes, donde se puede especificar que sea nulo o que se quede en blanco (blank) y se debe especificar una ruta donde se van a guardar las imagenes (upload_to)
> Para poder hacer uso de imagenes se debe instalar Pillow, _pip install Pillow_

## Enlace de la aplicación con el proyecto
Debemos señalarle al projecto de django que las aplicaciones que tengamos son del mismo proyecto, entonces tenemos que ir a settings.py y en la constante INSTALLED_APPS, agregamos el nombre de la aplicación, en este caso, productos.

Ahora hay que hacer una migración, para que se refresque la base de datos con la tabla que recién creamos a partir del modelo. Hacemos: _python3 manage.py makemigrations_ Con este comando django transforma el modelo y lo mete en una carpeta migrations y dentro hay archivos con las migraciones de los modelos.

Pero no se han visto aplicadas las tablas, solo se crearon los modelos. Hacemos: _python3 manage.py migrate_


## Dase de datos en el panel de administración
Ya con la tabla cargada, es posible ver e ingresar datos desde el endpoint de /admin, para que se pueda hacer esto, vamos a nuestro archivo admin.py de la aplicación y debemos registrar los modelos ya creados y aplicados.

Importamos la clase/modelo de .models y la añadimos con la linea _admin.site.register(MODELO)_

Y listo, esto debería mostrar el modelo en la ruta de administración.

Agregamos un producto y le damos en save, vemos que nos muestra un listado de productos, pero no muestra los nombres, sino objetos tipo productos, y esto se debe a que no se ha especificado que hacer cuando se imprima o se mande a llamar a una instancia de la clase. Esto se corrige sobreescribiendo el método str en la clase.

## Agregando los productos al endpoint index
Descargamos el html del curso 'list_of_products' que es la pura vista. Estos archivos van en la carpeta templates, pero esta carpeta templates puede ser una en cada aplicación o una al mismo nivel que el proyecto, esto ya depende de la arquitectura del proyecto.

Dentro de views.py, podemos llamar a todos los registros/elementos que se tienen en la base de datos. Para acceder a estos, obviamente lo importamos y accedemos a estos con el método: _Productos.objects.all()_, si quisieramos obtener un producto, podríamos hacerlo por su id con:"_Productos.objects.get(id=1)_, el where de la consulta sql se llama _filter_: _Productos.object.filter(name='Leche')_

Ya no retornamos una respuesta http con un hola mundo, sino un método render() en flask es render_template, y dentro del método render, como argumentos le pasamos el objeto request que recibimos como parámetro en la función index, el nombre del template html y un diccionario donde se encuentren todos los productos como respuesta de la consulta con el ORM.

Pero esto aún no está registrado en el proyecto, se escribío y modificó en la aplicación, pero falta actualizar el proyecto en sí.

Vamos a settings.py del proyecto, vamos a la constante _TEMPLATES_, contiene una lista de diccionarios, en la llave DIRS, van las carpetas/directorios donde se hallen los templates, en caso que hubiese un templates por aplicación se especifica: _nombre-aplicacion/templates_

> En los HTML no se usa Jinja, sino Djando templates. Es casi la misma mamada, se usan {{ }} o {% %}

## Modificando el html
Por defecto tiene 3 cartas, borramos 2 porque solo tenemos 1 producto, y creamos un for que envuelva la tarjeta, y dentro, en vez que diga producto 1, pues pasamos el nombre del producto, lo mismo con el precio. Para la imagen, en una etiqueta img, en el aributo src especificamos: _producto.imagen.url_ el objeto, la imagen. Pero esto todavía no muestra la imagen, falta modificar el urls.py del proyecto. Importamos static de la configuración de django y a la lista de la url le sumamos (literalmente) la función static, la cual recibe como argumentos la configuración (que debemos importar) donde especificamos que queremos acceder a los archivos multimedia, así como su direcció específica. Estos dos los toma del archivo settings.py

# Siguiente clase de Django

## Conectandonos a otra base de datos
Por defecto, django usa sqlite, pero acepta muchos tipos de motores de bases. [link de la documentación](https://docs.djangoproject.com/en/5.1/ref/databases/)

Usaremos MySQL para este ejemplo, entonces debemos crear la base de datos: _CREATE DATABASE nombre CHARACTER SET utf8;_

Dentro del archivo settings.py debemos especificar que queremos usar otra base de datos. Algo así:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/path/to/my.cnf",
        },
    }
}

Como vemos hay una llave para leer un archivo por defecto y su valor es un path. Pues es ahí donde debemos guardar los datos de la base, usuario, contraseña,... para la conexión a la base.

Pero ese archivo no existe. debemos crearlo y dentro hacemos:

[client]  
database = NAME  
user = USER  
password = PASSWORD  
default-character-set = utf8  

Por supuesto que colocando el nombre de la base y los datos que corresponden. y en settings debemos modificar el path para que apunte a este archivo.

Volvemos a correr el servidor y no debería dar problema. (Se debe instalar el motor de bases de datos anteriormente.) Pero nos da la adverterncia que no se han aplicado las migraciones de los datos. Hacemos: _python3 manage.py migrate_

No tenemos ningún superusuario ya que la base de datos está limpia.

## Configuración de ambientes de desarrollo
Normalmente existen 3:
- Desarrollo (development)
- Pruebas (QA-Testing)
- Producción (production)

Cada uno de estos tiene sus propias configuraciones, todo inicia en desarrollo, pero las otras dos tienen gran parte de sus características. 

Para las configuraciones específicas de los ambientes, se puede crear una carpeta y dentro archivos con las configuraciones, o solo un archivo y ahí dentro todas las configuraciones, o pedirle a una herramienta externa que nos configure o de la maqueta de las configuraciones, ...

Dentro de settings/base.py copiamos todo el contenido que había en el archivo settings.py del proyecto de django, también movemos a esta carpeta el archivo de my.cnf (lo agregamos al gitignore).

Creamos otros dos archivos que simbolizan los ambientes de desarrollo y producción.

Importamos todo de base en prodcuccion.py y cambiamos la configuración del debug a false. Y en el ambiente de desarrollo tenemos la configuración de la base de datos, la borramos de base y la colocamos en local.py
> Se debe modificar la ruta de la configuración del .cnf

En producción también colocamos la base de datos, pero la ruta del archivo .cnf es diferente.

Para que django tome estos archivos de configuracion debemos especificarle al momento de correr el servidor: _python manage.py runserver --settings=settings.local_ colocamos la bandera --settings y especificamos la ruta

## Nuevos modelos
Hasta el momento solo tenemos un modelo para los productos. Pues vamos a agregar modelos para los usuarios, marcas, comentarios y likes para los productos.

Para las llaves foraneas, se tiene un método y el primer argumento es el nombre de la clase a la cual se está haciendo referencia, y después especificamos en la propiedad on_delete el valor de CASCADE. Esto se escribe por si borramos un registro también se elimine la referencia. Como 3er argumento le damos un nombre a esta relación, el cual debe ser afin a la tabla donde se está escribiendo esta llave foránea.

Al terminar debemos hacer las migraciones correspondientes con _makemigrations_, peeeero, debemos especificarle donde está la configuración de la base de datos. Peeeero, ponerle la bandera _--settings_ a cada rato es un fastidio, así queeeee generamos un archivo __Makefile__, en cual podemos generar comandos abreviados, esto para evitar todo el fastidio de los comandos con las banderas y demás, o también pueden ser una lista de comandos. Generado el archivo y los comandos abriviados ahora hacemos: _make (comando)_

Si al hacer las migraciones hay problema, borramos los archivos generados al haecr el makemigrations, estos se encuentran en la carpeta migrations, y/o entrar a la base y borrar los datos (solo cuando son de prueba)

## Endpoint 'Leer mas'
Creamos la función dentro del view, para obtener un producto en específico. Luego vamos al urls.py donde están las url mapeadas y agregaremos la nueva ruta, para esta ruta agregamos otrao parámetro, que es el nombre con el cual se puede acceder a ese path desde cualquier aprte de la aplicación.

Se descarga el otro html para la vista correspondiente y se modifica conforme al contexto mandado por la view. También modificamos el html de la lista de productos, para que el botón de leer más, redireccione al producto. Esto con el atributo href, donde usaremos lenguaje de django templates y usaremos la propiedad _url_, en la cual hacemos referencia al nombre que le pusimos a la ruta, en urls.py y el id que esperamos recibir.

# Clase 3
## Templates y statics
Para ver este pedo del frontend y como se estrcutura más que nada. creamos un html base, ya que los dos archivos html que tenemos repiten información. Dentro de base.html tendremos el head, que es lo que se repite

Dentro del body colocamos con lenguaje de templates, muy similar a jinja2. block content y endblock dentro de llaves y signos de porcentaje. En los otros archivos heredamos de base y colocamos el bloque  de contenido.

Para los archivos de estilos, pues ya se sabe que deben ir en una carpeta llamada __static__, para referenciarlos en los html agregamos una etiqueta link y en el atributo href, agregamos la referencia. Pero esto no es suficiente para que se carguen los archivos css, debemos ir a las configuraciones del proyecto y debajo de la constante _STATIC URL_ agregamos la constante *STATICFILES_DIRS*, que contendrá una lista con un elemento que es una referencia a la constante BASE_DIR, que hace referencia al proyecto y colocamos el simbolo: / y después el nombre de la carpeta. esto se parece a una división pero bueno.

Y con esto debería cargar los archivos.
> Todos los archivos html deben tener al principio un load static, para cargar los css. Si hay archivos que heredan de otros, el archivo padre debe tener el load static y con eso.

Existen otros tipos de vistas pero ahora son clases en vez de una función.

Existe al página [ccbv.co.uk](https://ccbv.co.uk/) que nos regala views genéricas con todos los métodos y atributos de las vistas/clases.

Si se desea paginar nuestra lista de productos, en la documentación de django viene como hacerlo.

## Autorización y autenticación
En el panel de adminsitración tenemos un apartado de esto, parra agregar usuarios y grupos con diferentes permisos. 

Django ya viene con componentes para la [autenticación](https://docs.djangoproject.com/en/5.1/ref/contrib/auth/), existe la clase _User.model_ para tratar con esto. Campos, atributos y métodos que podemos ver desde el panel de administración.

Los templates se pueden mostrar cuando en el contexto ya se encuentra un usuario logeado. Lo podemos ver si agregamos un _{{ user }}_ en un template. Y se muestra el nombre del usuario actual. Y con este objeto user, podemos ejecutar varios métodos, como: _{{user.get_fullname }}_, es cuestión de checar la documentación.

Vamos a crear una nueva aplicación para gestionar las cuentas de los usuarios: _python3 manage.py startapp accounts_

Y debemos añadirla al proyecto, escribiendo su nombre en la variable INSTALLED_APPS en el archivo base.py

Vamos al proyecto cuentas y en la views implementamos una vista para el login. preguntamos si el método usado en la petición es post, sino mandamos el request y la redireccion al mismo template y como contexto un formulario que haremos después.

Ahora, en la carpeta de templates, agregamos una carpeta para las cuentas y dentro un login.html, para la vista que creamos recientemente. Dentro del html, solo extendemos de base y colocamos un bloque de contenido.

Esta vista debemos agregarla a las urls admitidas. Dentro de la carpeta cuentas, creamos el archivo urls.py, este archivo es identico al que tenemos en la otra app, modificando los valores de los paths. Pero falta agregarlas al proyecto en sí, entocnes vamos el urls del proeycto y agregamos la ruta. Dentro del path, en el primer parámetro, vemos que es un string, el cual se muestra en la url en el navegador, pues como cada aplicación va a tener la suya, podemos colocarle un nombre para ingresar a todas estas urls que puede tener la aplicación. Para acceder a esto desde el navegador solo hace falta escribir el nombre que se colocó.

Después de comprobar que la ruta existe en el navegador, procedemos a crear el fomrulario que mandamos, el valor del formulario es uno que django posee dentro de sus librerías. Es un formulario de autenticación ya integrado, lo almacenamos en una variable la cual se pasará como contexto. Y en el html correspondiente, lo mandamos llamar.

Dentro de la lógica de la vista, en el caso donde el método sea post, debemos cachar la información que mande el usuario, y dentro de los parámetros del método que django nos regala, le mandamos el objeto request.POST, que es la información recibida por el usuario. Se debe especificar que este objeto request.POST es el valor del objeto data.

Después preguntamos si el formulario es valido, con un método de django. Se considera valido cuando los campos obligatorios son cumplidos, las especificaciones de algunos campos son cumplidas, ... Si es valido, obtenemos el usuario con un método django y con otro método, logeamos manualmente al usuario. A este método login le pasamos el objeto request y el objeto user. Y para finalizar, redireccionamos a la página principal, igualmente con un método que nos regala django.

Para el logout, igualmente hacemos una función y usamos el método asociado de django. Y también esta view la registramos en las urls. Vamos a base.html y tomamos una barra de navegación sencilla de bootstrap, la pegamos y modificamos para que haya un botón dentro de un formulario, el cual tiene la acción de redirigir cuando se pulse.

Dentro del html agregamos una condicional, si el usuario ya esta autenticado, pues mostramos la barra con el botón, sino mostramos otro botón de inicio de sesión.

# Clase 4
## Formularios y Validaciones
Antes de empezar con lo bueno, hay que hacer una modificación al html. mandaremos la barra de navegación a un archivo independiente y lo mandaremos a llamar con la propiedad _{% includes 'ruta' %}_ el cual importa el contenido de un archivo y lo coloca en donde es llamado. La ruta debe incluir la carpeta donde se encuentra, ya que django busca en la carpeta templates solamante.

Crearemos formularios para los comentarios de cada producto de la tienda. Entonces empezamos creando el modelo de los comentarios. Esto en la carpeta de productos. para el producto, hacemos una llave foranea y dentro especificamos el nombre de la aplicación y el nombre del modelo, en este caso productos.Producto. Los demás columnas son legibles en el código. Agregamos una función para ver si el comentario fue aprobado, si sí, se guarda en la base con un método de django.

Hacemos las migraciones correspondientes con los dos comandos de esto. Y agregamos en admin.py el nombre del modelo.