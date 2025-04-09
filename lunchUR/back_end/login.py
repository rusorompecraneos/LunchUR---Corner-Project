from django.contrib import messages
from django.shortcuts import render, redirect
from mi_admin.models import usuarios
from django.views import View

#Clase creada para que el usuario se loguee correctamente
class Login_usuario(View):
    def get(self, request):
        #Muestra el formulario para registrarse
        return render(request, 'Registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            usuario = usuarios.objects.get(correo_electronico=username, contraseña=password)
            # Guardamos el ID del usuario en la sesión
            request.session['usuario_id'] = usuario.numero_id
            request.session['nombre_usuario'] = usuario.nombre
            messages.success(request, f"Bienvenido {usuario.nombre} 😊")
            return redirect('home')  
        except usuarios.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('login')
            
        