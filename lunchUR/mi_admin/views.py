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

# Create your views here.

#Clase creada para que el usuario se loguee correctamente
class LoginUsuario(LoginView):
        template_name = 'Registration/login.html'
        next_page = reverse_lazy('inicio')
        
        
#Clase para que el usuario se resgistre por primera vez. 
registro_view = RegistroView()   #Instancia creada para poder llamar a la clase. 
def mi_vista_personalizada(request):
    return RegistroView.as_view()(request) 
    

class inicio(View):
    template_name = 'Inicio/inicio.html'
    def get(self, request):
        return render(request, self.template_name)
    

class Lista_de_precios(View):
    template_name = 'Inicio/lista_de_precios.html'
    def get(self, request):
        return render(request, self.template_name)
            
# Funcion para ver las ofertas del dia. 
def ofertas_del_dia(request):
    ofertas = ofertas_del_dia()  # Llama la función del otro archivo
    return render(request, 'ofertas.html', {'ofertas': ofertas})


    
    

    
    