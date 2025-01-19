from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.CharField(max_length=10)

    categoria = models.CharField(max_length=50)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField(upload_to='img/productos', null=True, blank=True)

    descuento = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f'{self.nombre} | {self.marca} | {self.precio}'


class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    descuento = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to='img/marcas', null=True, blank=True)

    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Comentarios(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.CharField(max_length=200)

    comentario = models.TextField()

    fecha_creacion = models.DateTimeField(default=timezone.now)
    comentario_aprobado = models.BooleanField(default=False)

    def aprobar_comentario(self):
        self.comentario_aprobado = True
        self.save()

    def __str__(self):
        return self.comentario