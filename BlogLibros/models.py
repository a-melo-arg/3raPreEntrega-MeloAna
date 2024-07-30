from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    genero = models.CharField(max_length=30)
    
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
        
class Lectores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)

