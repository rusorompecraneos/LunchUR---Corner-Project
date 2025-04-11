from django.db import models
from django.utils import timezone


# Create your models here.
class usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default = 'Null')
    numero_id = models.IntegerField(unique=True)
    correo_electronico = models.EmailField(unique=True, max_length=60, null=False, blank=False)
    contraseña = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nombre

#acá se guardan los datos de la oferta
class Oferta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    descuento = models.FloatField()  #Descuento en porcentaje 
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def esta_activa(self): #verifica si la oferta está 
        """verifica si la oferta está vigente """
        hoy = timezone.now().date()
        return self.fecha_inicio <= hoy <= self.fecha_fin
    
    def __str__(self):
        return self.titulo
    
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

    
class CanalDeApoyo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace = models.URLField()

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=[
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada')
    ], default='CONFIRMADA')
    
    class Meta:
        verbose_name_plural = "Reservas"
        
    def __str__(self):
        return f"Reserva de {self.usuario.nombre} para {self.fecha_reserva}"

    
class PerfilUsuario(models.Model):
    ROLES = [
        ('cliente', 'Cliente'), #el primer valor es lo que se guarda en la base de datos, el segundo valor es lo que se muestra en los formularios 
        ('administrativo', 'Administrativo'),
        ('empleado', 'Empleado'),
    ]
    #Relación con el modelo de usuario de Django 
    User = models.OneToOneField(usuarios, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=20, unique=True) #id para identificar a cada usuario
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente') #se almacena el rol del usuario

    def __str__(self):
        return f"{self.user.username} - {self.rol}"

    
    
       