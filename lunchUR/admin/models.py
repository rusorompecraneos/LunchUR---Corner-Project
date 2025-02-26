from django.db import models

# Create your models here.
class usuarios(models.Model):  
    nombre = models.CharField(max_length=50)
    alias = models.CharField(max_length=100)
    poder = models.IntegerField()
    
class menus(models.Model):
    nombre_menu = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    icono = models.CharField(max_length=200)
    
    