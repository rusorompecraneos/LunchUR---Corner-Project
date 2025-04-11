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
        id = request.POST.get('Numero_de_id')
        
        try:
            usuario_encontrado = usuarios.objects.get(correo_electronico=username, contraseña=password, numero_id = id)
            # Guardamos el ID del usuario en la sesión
            request.session['numero_id'] = usuario_encontrado.numero_id
            request.session['nombre_usuario'] = usuario_encontrado.nombre
            messages.success(request, f"Bienvenido {usuario_encontrado.nombre} 😊")
            return redirect('home')  
        except usuarios.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('login')
        
            
        