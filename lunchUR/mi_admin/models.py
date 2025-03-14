from django.db import models


# Create your models here.
class usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default = 'Null')
    numero_id = models.IntegerField()
    correo_electronico = models.EmailField(unique=True, max_length=60, null=False, blank=False)
    contraseña = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class menus(models.Model):
    nombre_menu = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_menu
    
class alimentos_menu(models.Model):
    num_alimentos = models.IntegerField(null=True, blank=True)
    proteina_menu = models.CharField(null=True, blank=True)
    carbohidratos_menu = models.CharField(null=True, blank=True)
    grasas_menu = models.CharField(null=True, blank=True)
    ensaldas_menu = models.CharField(null=True, blank=True)

    def __str__(self):
        return str(self.num_alimentos)      # Se convierte a string para evitar un error de type 
        
    
class planes_alimenticios(models.Model):
    tipo_plan = models.CharField(max_length=30, null=True, blank=True)
    descripcion_plan = models.CharField(max_length=200, null=True, blank=True)
    precio_plan = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.tipo_plan

class reservas(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    
    def __str__(self):
        return self.usuario.nombre

    
    
    
       