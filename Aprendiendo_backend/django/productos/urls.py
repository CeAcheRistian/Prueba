from django.contrib import admin
from django.urls import path

from .views import index, obtener_producto

urlpatterns = [
    path('', index),
    path('producto/<int:id>/', obtener_producto, name='obtener_producto'),
]
