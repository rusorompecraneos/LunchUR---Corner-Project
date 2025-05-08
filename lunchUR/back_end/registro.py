from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from mi_admin.models import usuarios

class RegistroView(View):
    def get(self, request):
        return render(request, 'Registration/registro.html')

    def post(self, request):
        if request.method == "POST":
            nombre = request.POST.get('nombre', '').strip()
            apellido = request.POST.get('apellido', '').strip()
            numero_id = request.POST.get('numero_id', '').strip()
            correo_electronico = request.POST.get('correo', '').strip()
            contraseña = request.POST.get('password', '').strip()

            # Verifica campos vacíos
            if not all([nombre, apellido, numero_id, correo_electronico, contraseña]):
                messages.error(request, "Todos los campos son obligatorios.")
                return redirect('registro')

            # Validamos que el número de documento sea numérico
            try:
                numero_id_int = int(numero_id)
            except ValueError:
                messages.error(request, "❌ El número de documento debe contener solo números.")
                return redirect('registro')

            # Validamos longitud máxima del documento
            if len(numero_id) > 20:
                messages.error(request, "⚠️ El número de documento no puede tener más de 20 dígitos.")
                return redirect('registro')

            # Validamos la unicidad del correo electronico. 
            if usuarios.objects.filter(correo_electronico=correo_electronico).exists():
                messages.error(request, "¡El correo ya está registrado! Por favor registra un correo válido.")
                return redirect('registro')

            # Validamos la unicidad del documento. 
            if usuarios.objects.filter(numero_id=numero_id).exists():
                messages.error(request, "¡El número de documento ya está registrado!")
                return redirect('registro')

            # Validamos longitud de contraseña
            if len(contraseña) < 6:
                messages.error(request, "¡La contraseña debe tener al menos 6 caracteres!")
                return redirect('registro')

            # Creamos la cuenta de usuario y lo guardamos en el moedelo de usuarios.
            nuevo_usuario = usuarios(
                nombre=nombre,
                apellido=apellido,
                numero_id=numero_id_int,
                correo_electronico=correo_electronico,
                contraseña=contraseña
            )
            nuevo_usuario.save()

            request.session['numero_id'] = nuevo_usuario.numero_id

            messages.success(request, "¡Ya estás dentro rosarista! Ahora puedes iniciar sesión.")
            return redirect('login')  #Redirigeal usuario al login

        