from django.urls import path
from BlogLibros import views

urlpatterns = [    
    path('', views.inicio),
    path('cargarlibro', views.cargar_libro),
    path('buscar_libro', views.buscar_libro),
    path('busquedaLibro', views.busquedaLibro),
    path('cargarautor', views.cargar_autor),
    path('cargarlector', views.cargar_lector),
    
]