from django.shortcuts import render

from django.http import HttpResponse
from .models import Libro, Autor, Lectores
from .forms import LibroFormulario, BusquedaFormulario, AutorFormulario, LectorFormulario

def inicio(request):
    return render(request, "BlogLibros/inicio.html")

def cargar_libro(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST) # Aqui me llega la informacion del html
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            libro = Libro(titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"])
            libro.save()
            return render(request, "BlogLibros/inicio.html")  # vuelvo a inicio
    else:
        miFormulario = LibroFormulario()  # formulario vacio para construir el html
    return render(request, "BlogLibros/cargarlibro.html", {"miFormulario": miFormulario})


def busquedaLibro(request):
    return render(request, "BlogLibros/buscarlibro.html")

def buscar_libro(request):   #busca en la BD
    if request.GET ["librobuscado"]:
        librobusco = request.GET ["librobuscado"]
        libros = Libro.objects.filter(titulo__icontains=librobusco)
            
        return render(request, "BlogLibros/mostrarlibros.html", {"titulo":librobusco, "libros":libros})  
    else:
        respuesta = "ERROR, por favor ingrese el nombre del libro"
        return HttpResponse(respuesta)

def cargar_autor(request):
    if request.method == "POST":
        miFormulario = AutorFormulario(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            autor = Autor(nombre=informacion["nombre"], apellido=informacion["apellido"],)
            autor.save()
            return render(request, "BlogLibros/inicio.html")  
    else:
        miFormulario = AutorFormulario()  
    return render(request, "BlogLibros/cargarautor.html", {"miFormulario": miFormulario})

def cargar_lector(request):
    if request.method == "POST":
        miFormulario = LectorFormulario(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            lector = Lectores(nombre=informacion["nombre"], apellido=informacion["apellido"], pais=informacion["pais"])
            lector.save()
            return render(request, "BlogLibros/inicio.html")  
    else:
        miFormulario = LectorFormulario()  
    return render(request, "BlogLibros/cargarlector.html", {"miFormulario": miFormulario})