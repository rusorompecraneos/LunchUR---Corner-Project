from django.shortcuts import render, redirect
from mi_admin.models import usuarios
from django.views import View


#Funcion para mostrar el perfil del usuario. (Luego de la implementacion del CSS, se arreglo el problema que habia. ). 
class Perfil_usuario(View):
    def get(self, request):
        numero_id = request.session.get('numero_id')

        if not numero_id:
            return redirect('login')

        try:
            usuario = usuarios.objects.get(numero_id=numero_id)
            return render(request, 'perfil_usuario.html', {'perfil': usuario})
        except usuarios.DoesNotExist:
            return redirect('login')
    
    