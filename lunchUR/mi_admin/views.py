 #En la carpeta "mi_admin" se crea una carpeta llamada "Templates" para que el front (html y css).
 #Aqui va el back
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import usuarios
from django.contrib.auth.hashers import make_password #importamos la funcion para hashear las contraseñas.
from django.views import View
from back_end.registro import RegistroView
from back_end.funciones import ofertas_del_dia 
from .models import CanalDeApoyo
from .models import PerfilUsuario
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#Clase creada para que el usuario se loguee correctamente
class LoginUsuario(LoginView):
        template_name = 'Registration/login.html'
        next_page = reverse_lazy('inicio')
        
        
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
        precios = [
            ("Ensalada energetica ", "$12.000"),
            ("Bowl gladiador ", "$15.000"),
            ("Mega muscle plato ", "$15.000"),
            ("Hamgurguesa artesanal ", "$14.000"),
            ("Estofado casero ", "$13.500"),
            ("Tortilla saludable  ","$12.000"),
            ("Pasta tradicional ", "$14.500"),
            ("Menu criollo ", "$14.000"),
            ("Bolw proteico ", "$16.000"),
            ("Menu marino ", "$15.800"),
            ("Clasico casero ", "$13.000"),
        
    ]
        
        return render(request, 'nuestros_productos.html', {'precios': precios})
            
# Funcion para ver las ofertas del dia. 
def ofertas_del_dia(request):  # request es obligatorio como primer argumento
    return render(request, 'ofertas.html')

# Funcion para visualizar el html de los canales de apoyo. 
def canales_apoyo(request):
    canales = CanalDeApoyo.objects.all()
    return render(request, 'canales_de_apoyo.html', {'canales': canales})

#Clase para visualizar la pagina "home".
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['nombre'] = usuario.first_name
        return context    
    

    #Funcion para mostrar el perfil del usuario. 
@login_required #está verificando que esté autenticado
def perfil_usuario(request): 
    perfil = PerfilUsuario.objects.get(user=request.user)
    return render(request, 'perfil_usuario.html', {'perfil': perfil})
    #se obtiene el perfil del usuario actual y lo envia a la plantilla



    
    