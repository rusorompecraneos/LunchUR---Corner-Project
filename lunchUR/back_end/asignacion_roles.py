from django.db import models
from mi_admin.models import usuarios
from mi_admin.models import PerfilUsuario

def verificacion(request):
    if request.method == "POST":  # Verificamos que la solicitud sea POST
        rol = request.POST.get('rol', 'cliente')  # Si no se selecciona, se asigna "cliente" por defecto
        
        # Obtener el usuario autenticado
        usuario = request.user  # Suponiendo que el usuario está autenticado
        
        # Obtener el número de documento desde el formulario
        numero_id = request.POST.get('numero_documento')  # Asegúrate de que el input en HTML tenga el name="numero_documento"
        
        # Crear un nuevo perfil
        nuevo_perfil = PerfilUsuario.objects.create(
            user=usuario,  # Corregido de "usuarios" a "usuario"
            numero_documento=numero_id,  # Ahora está definido correctamente
            rol=rol
        )

        