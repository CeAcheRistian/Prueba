from django.contrib import admin
from .models import Producto, Marca, Comentarios

# Register your models here.

admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Comentarios)