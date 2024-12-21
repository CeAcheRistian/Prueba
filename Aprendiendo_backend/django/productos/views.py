from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto

# Create your views here.

def index(request):
    productos = Producto.objects.all()

    return render(request, 'list_of_products.html', {'productos': productos})

def obtener_producto(request, id):
    producto = Producto.objects.get(id=id)

    return render(request, 'show_product.html', {'producto': producto})