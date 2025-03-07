from django.db import models

# Create your models here.
class usuarios(models.Model):
    nombre = models.CharField(max_length=60)
    numero_id = models.IntegerField(max_length=30)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=30)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class menus(models.Model):
    nombre_menu = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_menu
    
class alimentos_menu(models.Model):
    num_alimentos = models.IntegerField()
    ensaladas_nombre = models.CharField(max_length=20)
    vegetales_nombre = models.CharField(max_length=20)
    postres_nombre = models.CharField(max_length=20)
    bebidas_nombre = models.CharField(max_length=20)
    carnes_nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.num_alimentos
        
    
class planes_alimenticios(models.Model):
    plan_fit = models.CharField()
    plan_normal = models.CharField()
    plan_vegetariano = models.CharField()
    plan_vegano = models.CharField()
    
    def __str__(self):
        return self.plan_fit

class reservas(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    
    def __str__(self):
        return self.usuario.nombre



    
       