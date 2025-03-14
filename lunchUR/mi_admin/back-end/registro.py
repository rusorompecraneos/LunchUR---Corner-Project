from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views import View
from mi_admin.models import usuarios

class RegistroView(View):
    def get(self, request):
        #Muestra el formulario para registrarse
        return render(request, 'registro.html')

    def post(self, request):
        #va a procesar el formulario de registro con las respectivas validaciones
        if request.method == "POST":
            nombre = request.POST.get('nombre').strip()
            apellido = request.POST.get('apellido').strip()
            numero_documento = request.POST.get('numero_documento').strip()
            correo_electronico = request.POST.get('correo').strip()
            contraseña = request.POST.get('password').strip()

        #hace parte de la validación, verifica que los campos no estén vacíos
        if not all([nombre, apellido, numero_documento, correo_electronico, contraseña]):
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('registro')

        #El correo debe ser único
        if User.objects.filter(email=correo_electronico).exists():
            messages.error(request, "¡El correo ya está registrado!")
            return redirect('registro')

        #El número de documento debe ser único
        if usuarios.objects.filter(numero_documento=numero_documento).exists():
            messages.error(request, "¡El número de documento ya está registrado!")
            return redirect('registro')

        #La contraseña debe tener al menos 8 caracteres
        if len(contraseña) < 6:
            messages.error(request, "¡La contraseña debe tener al menos 6 caracteres!")
            return redirect('registro')

        #Crear el usuario
        nuevo_usuario = usuarios(
            nombre=nombre,
            numero_id=numero_documento,
            correo_electronico=correo_electronico,  # Verifica que el nombre sea EXACTAMENTE igual al modelo
            contraseña=contraseña
        )
        nuevo_usuario.save()

        #Crear perfil de usuario adicional si es necesario
        usuarios.objects.create(
            user=nuevo_usuario,
            numero_documento=numero_documento
        )

        messages.success(request, "¡Ya estás dentro rosarista! Ahora puedes iniciar sesión.")
        return redirect('login')  #Redirigeal usuario al login
