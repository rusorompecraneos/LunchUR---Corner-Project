 #En la carpeta "mi_admin" se crea una carpeta llamada "Templates" para que el front (html y css).
 #Aqui va el back
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password #importamos la funcion para hashear las contraseñas.
from django.views import View
from back_end.registro import RegistroView
from .models import CanalDeApoyo
from back_end.login import Login_usuario
from back_end.home import HomeView
from back_end.reservas import Reservas_Almuerzos
from back_end.plan import PlanNutricional
from back_end.productos_populares import Productos_populares
from back_end.historial_de_compras import Historial_de_compras
from back_end.boton_reservas import BotonReservas
from back_end.perfil_usuario import Perfil_usuario

        
#Llamamos a la funcion de login. 
login_view = Login_usuario()   #Instancia creada para poder llamar a la clase. 
def mi_vista_personalizada(request):
    return Login_usuario.as_view()(request)         
        

#Clase para que el usuario se resgistre por primera vez. 
registro_view = RegistroView()   #Instancia creada para poder llamar a la clase. 
def mi_vista_personalizada(request):
    return RegistroView.as_view()(request) 
    
#Clase de inicio 
class inicio(View):
    template_name = 'Inicio/inicio.html'
    def get(self, request):
        return render(request, self.template_name)

#Clase creada para visualizar los precios y productos. 
class Nuestros_productos(View):    
    def get(self, request):
        productos = [
            ("Ensalada energética", "Mix de hojas verdes, garbanzos, quinoa, aguacate, con aderezo de mostaza y miel", "$12.000"),
            ("Bowl gladiador", "Pechuga de pavo con garbanzos, arroz integral y espinaca, aderezado con crema de yogur y mostaza", "$15.000"),
            ("Mega muscle plato", "Pechuga de pollo al grill con camote asado, brócoli al vapor y una porción de arroz integral", "$15.000"),
            ("Hamburguesa artesanal", "Hamburguesa de res o pollo con lechuga, tomate y aderezo especial, con papas al horno y salsa secreta de Mike", "$14.000"),
            ("Estofado casero", "Carne de res cocida a fuego lento con papas, zanahorias y guisantes, acompañada de arroz blanco", "$13.500"),
            ("Tortilla saludable", "Tortilla de espinaca y queso, acompañada de pan integral y guacamole", "$12.000"),
            ("Pasta tradicional", "Espaguetis en salsa boloñesa, arroz integral, acompañados de pan de ajo y una ensalada", "$14.500"),
            ("Menú criollo", "Lomo saltado con papas fritas y arroz, servido con una porción de crema huancaína", "$14.000"),
            ("Bowl proteico", "Arroz integral con pollo, aguacate, huevo frito, lomo de carne y aderezo de yogur", "$16.000"),
            ("Menú marino", "Filete de pescado a la plancha con puré de camote, ensalada y una rodaja de limón y bebida", "$15.800"),
            ("Clásico casero", "Jugoso filete de res o pollo a la plancha, acompañado de arroz, ensalada fresca y puré de papas", "$13.000"),
        ]
        
        return render(request, 'nuestros_productos.html', {'productos': productos})

# Funcion para ver las ofertas del dia. 
def ofertas_del_dia(request):  # request es obligatorio como primer argumento
    return render(request, 'ofertas.html')

# Funcion para visualizar el html de los canales de apoyo. 
def canales_apoyo(request):
    canales = CanalDeApoyo.objects.all()
    return render(request, 'canales_de_apoyo.html', {'canales': canales})

#Instanciamos la clase para visualizar el home
home_view = HomeView()   #Instancia creada para poder llamar a la clase. 
def mi_vista_personalizada(request):
    return HomeView.as_view()(request)         
        
    
# Instancia para llamar a la clase que contiene las reservas. 
reservas_view = Reservas_Almuerzos()  
def mi_vista_personalizada(request):
    return Reservas_Almuerzos.as_view()(request)

# Intancia para llamar a la clase para que el usuario pueda acceder a su perfil.
perfil_usuario_view = Perfil_usuario()  
def mi_vista_personalizada(request):
    return Perfil_usuario.as_view()(request)
    
#Instanciamos para poder ver el plan de alimentos. 
planes_alimentacion_view = PlanNutricional()  
def mi_vista_personalizada(request):
    return PlanNutricional.as_view()(request)

# vista para productos populares
productos_populares_view = Productos_populares()  
def mi_vista_personalizada(request):
    return Productos_populares.as_view()(request)

# vista para el historial de compras
historial_de_compras_s_view = Historial_de_compras()  
def mi_vista_personalizada(request):
    return Historial_de_compras.as_view()(request)

# vista para el boton de reservas
boton_reservas_view = BotonReservas()  
def mi_vista_personalizada(request):
    return BotonReservas.as_view()(request)



