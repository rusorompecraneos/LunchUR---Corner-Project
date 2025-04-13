from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views import View
from mi_admin.models import usuarios
from django.utils.translation import ngettext


class RegistroView(View):
    def get(self, request):
        #Muestra el formulario para registrarse
        return render(request, 'Registration/registro.html')

    def post(self, request):
        #va a procesar el formulario de registro con las respectivas validaciones
        if request.method == "POST":
            nombre = request.POST.get('nombre').strip()
            apellido = request.POST.get('apellido').strip()
            numero_id = request.POST.get('numero_id').strip()
            correo_electronico = request.POST.get('correo').strip()
            contraseña = request.POST.get('password').strip()

        #hace parte de la validación, verifica que los campos no estén vacíos
        if not all([nombre, apellido, numero_id, correo_electronico, contraseña, numero_id]):
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('registro')

        #El correo debe ser único
        if usuarios.objects.filter(correo_electronico=correo_electronico).exists():
            messages.error(request, "¡El correo ya está registrado! Por favor registra un correo valido")
            return redirect('registro')

        #El número de documento debe ser único
        if usuarios.objects.filter(numero_id=numero_id).exists():
            messages.error(request, "¡El número de documento ya está registrado! Por favor ingresa uno valido. ")
            return redirect('registro')

        #La contraseña debe tener al menos 8 caracteres
        if len(contraseña) < 6:
            messages.error(request, "¡La contraseña debe tener al menos 6 caracteres!")
            return redirect('registro')

        # Crear el usuario
        nuevo_usuario = usuarios(
        nombre=nombre,
        apellido=apellido,
        numero_id=numero_id,
        correo_electronico=correo_electronico,
        contraseña=contraseña
    )
        nuevo_usuario.save()
        
        
        request.session['numero_id'] = nuevo_usuario.numero_id


        messages.success(request, "¡Ya estás dentro rosarista! Ahora puedes iniciar sesión.")
        return redirect('login')  #Redirigeal usuario al login

        