from django.shortcuts import render
from mi_admin.models import Producto
from django.views import View

# Clase que solo redirige al productos_populares.html
class Productos_populares(View):
    def get(self, request):
        productos_populares = Producto.objects.all()  # Aquí podrías aplicar filtros si es necesario
        return render(request, 'productos_populares.html', {'productos_populares': productos_populares})
