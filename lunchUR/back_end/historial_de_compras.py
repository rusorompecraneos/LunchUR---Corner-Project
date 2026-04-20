from django.shortcuts import render
from mi_admin.models import Compra, usuarios
from django.views import View



class Historial_de_compras(View):
    def get(self, request):
        usuario_id = request.session.get('usuario_id')  # ID guardado en sesión tras login o registro

        if usuario_id is not None:
            try:
                usuario = usuarios.objects.get(id=usuario_id)
                compras = Compra.objects.filter(usuario=usuario).order_by('-fecha_compra')
                return render(request, 'historial_de_compras.html', {'compras': compras})
            except usuarios.DoesNotExist:
                return render(request, 'historial_de_compras.html', {'compras': [], 'error': 'Usuario no encontrado.'})
        else:
            return render(request, 'historial_de_compras.html', {'compras': [], 'error': 'ID de usuario no disponible.'})