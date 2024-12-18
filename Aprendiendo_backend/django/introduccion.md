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