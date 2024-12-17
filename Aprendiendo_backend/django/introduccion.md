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