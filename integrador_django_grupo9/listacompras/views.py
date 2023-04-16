"""
Módulo vistas
"""
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """ Función para la página de inicio de la app.
    Contiene la portada y ¿el menú principal?  
    :return: Render de la página de inicio.
    """
    return HttpResponse("Lista de compras - Página principal")

def articulos(request):
    """ Función para el CRUD de artículos.
    Presenta una grilla con las funciones CRUD para los artículos.
    :return: Render de la página de CRUD de artículos.
    """
    return HttpResponse("CRUD Artículos")

def tiendas(request):
    """ Función para el CRUD de tiendas.
    Presenta una grilla con las funciones CRUD para los tiendas.
    :return: Render de la página de CRUD de tiendas.
    """
    return HttpResponse("CRUD tiendas")

def listas(request):
    """ Función para el CRUD de listas.
    Presenta una grilla con las funciones CRUD para los listas.
    :return: Render de la página de CRUD de listas.
    """
    return HttpResponse("CRUD listas")

def irdecompras(request, id_lista):
    """ Función ver la lista de compras al momento de comprar.
    Presenta una grilla con la lista de compras seleccionada y por cada artículo un 
    checkbox que le permite al usuario ir marcando el artículo que ya fue comprado.
    :param IdLista: Recibe el id de la lista que se devolverá como lista para hacer la 
    compra.
    :return: Render de la lista para hacer las compras.
    """
    return HttpResponse(f"Lista hacer las compras id: {id_lista}")
