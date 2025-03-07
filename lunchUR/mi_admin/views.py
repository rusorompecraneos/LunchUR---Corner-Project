 #En la carpeta "mi_admin" se crea una carpeta llamada "Templates" para que el front (html y css).
 #Aqui va el back
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import usuarios
from django.contrib.auth.hashers import make_password #importamos la funcion para hashear las contraseñas.
from django.views import View

# Create your views here.


#Vista de prueba para confirmar la funcionalidad
def mi_vista(request):
    return HttpResponse("¡Hola, bienvenido a LunchUR! Donde podras gestionar tus almuerzos, cuando quieras y desde cualquier lugar")

#Clase creada para que el usuario se loguee correctamente
class LoginUsuario(LoginView):
        template_name = 'Registration/login.html'
        next_page = reverse_lazy('home')
        
#Clase para que el usuario se resgistre por primera vez. 
class RegistroUsuario(View):
        template_name = 'registration/registro.html'

        def get(self, request):
            return render(request, self.template_name)

        def post(self, request):
            nombre = request.POST.get('nombre')
            numero_documento = request.POST.get('numero_documento')
            correo_electronico = request.POST.get('correo_electronico')
            password = request.POST.get('password')

            usuarios.objects.create(
                nombre=nombre,
                numero_id=numero_documento,
                correo_electronico=correo_electronico,
                contraseña=make_password(password) #hasheamos la contraseña.
            )
            return redirect('login') #redirigimos al usuario a la pagina de login.
                  
