from django.db import models

# Create your models here.
class usuarios(models.Model):  
    nombre = models.CharField(max_length=60)
    numero_id = models.IntegerField(max_length=20)
    
    
class menus(models.Model):
    nombre_menu = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)


class alimentos(models.Model):
    ensaladas_nombre = models.CharField(max_length=20)
    vegetales_nombre = models.CharField(max_length=20)
    postres_nombre = models.CharField(max_length=20)
    bebidas_nombre = models.CharField(max_length=20)
    carnes_nombre = models.CharField(max_length=20)
    
    
       